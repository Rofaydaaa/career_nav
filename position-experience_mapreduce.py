from mrjob.job import MRJob
from mrjob.step import MRStep

class MRPositiontoExperience(MRJob):

    def mapper_position_to_experience(self, _, line):
        line_cols = line.split('¶')  # splitting the line into each field by the delimitter that I have added while generating the txt file 
        yield ((line_cols[6], line_cols[21]),1)  #yielding the column chosen, here we are choosing the field orgCompany_nameOrg to find the most mentioned organization 

    # def mapoper_position_experience_count(self,position,experience):
    #     yield ()

    def combiner_count_position_to_experience(self, postoexp, counts):
        # sum the companies we've seen so far
        yield (postoexp, sum(counts))

    def reducer_count_position_to_experience(self, postoexp, counts):
        # send all (num_occurrences, company) pairs to the same reducer.
        # num_occurrences is so we can easily use Python's max() function.
        yield None, (sum(counts), postoexp)

    # discard the key; it is just None
    def reducer_find_max_position_to_experience(self, _, postoexp_count_pairs):
        # each item of company_count_pairs is (count, company),
        # so yielding one results in key=counts, value=company
        try:
            yield max(postoexp_count_pairs)
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
    MRPositiontoExperience.run()
