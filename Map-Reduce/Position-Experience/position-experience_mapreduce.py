from mrjob.job import MRJob
from mrjob.step import MRStep

class MRPositiontoExperience(MRJob):

    def mapper_position_to_experience(self, _, line):
        line_cols = line.split('¶')  # splitting the line into each field by the delimitter that I have added while generating the txt file 
        yield (line_cols[0],( line_cols[1],1) ) #yielding the column chosen, here we are choosing the field orgCompany_nameOrg to find the most mentioned organization 

    # def mapoper_position_experience_count(self,position,experience):
    #     yield ()

    def combiner_count_position_to_experience(self, position, expcounts):
        experience_sum = 0
        for experience, count in expcounts:
            experience_sum += count  
            yield (position, (experience,experience_sum))

    def reducer_count_position_to_experience(self, position, expcounts):
        experience_sum = 0
        for experience, count in expcounts:
            experience_sum += count  
            yield (position, (experience_sum,experience))

    def reducer_find_most_experience_required_to_every_position(self, position, exper_count_pairs):
        try:
            max_count=0
            exp=None
            for count,experience in exper_count_pairs:
                if count>max_count:
                    max_count=count
                    exp=experience
            yield position, exp
        except ValueError:
            pass

    def steps(self):
        return [
            MRStep(mapper=self.mapper_position_to_experience,
                   combiner=self.combiner_count_position_to_experience,
                   reducer=self.reducer_count_position_to_experience),
            MRStep(reducer=self.reducer_find_most_experience_required_to_every_position)
        ]


if __name__ == '__main__':
    MRPositiontoExperience.run()
