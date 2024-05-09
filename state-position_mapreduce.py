from mrjob.job import MRJob
from mrjob.step import MRStep

class MRStateToPosition(MRJob):

    def mapper_position_to_experience(self, _, line):
        line_cols = line.split('¶')  # splitting the line into each field by the delimitter that I have added while generating the txt file 
        yield line_cols[10],(line_cols[6],1)  #yielding the column chosen, here we are choosing the field orgCompany_nameOrg to find the most mentioned organization 

    # def mapoper_position_experience_count(self,position,experience):
    #     yield ()

    def combiner_count_position_to_experience(self, state, position_count):
        # sum the companies we've seen so far
        position_sum = 0
        for position, count in position_count:
            position_sum += count  # Accumulate the counts
            yield (state, (position,position_sum))

    def reducer_count_position_to_experience(self, state, position_count):
        # send all (num_occurrences, company) pairs to the same reducer.
        # num_occurrences is so we can easily use Python's max() function.
        position_sum = 0
        for position, count in position_count:
            position_sum += count  # Accumulate the counts
        yield state, (position_sum, position)

    # discard the key; it is just None
    def reducer_find_max_position_to_experience(self, state, postoexp_count_pairs):
        # each item of company_count_pairs is (count, company),
        # so yielding one results in key=counts, value=company
        try:
            max_count=0
            pos=None
            for count,position in postoexp_count_pairs:
                if count>max_count:
                    max_count=count
                    pos=position
            yield state, pos
        except ValueError:
            pass

    def steps(self):
        return [
            MRStep(mapper=self.mapper_position_to_experience,
                   combiner=self.combiner_count_position_to_experience,
                   reducer=self.reducer_count_position_to_experience),
            MRStep(reducer=self.reducer_find_max_position_to_experience)
        ]


if __name__ == '__main__':
    MRStateToPosition.run()
