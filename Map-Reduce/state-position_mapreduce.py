from mrjob.job import MRJob
from mrjob.step import MRStep
import subprocess

class MRStateToPosition(MRJob):

    def mapper_state_to_position(self, _, line):
        line_cols = line.split('¶')  # splitting the line into each field by the delimitter that I have added while generating the txt file 
        yield line_cols[8],(line_cols[4],1)  #yielding the column chosen, here we are choosing the field orgAddress_addressline (8) and position(4) to find the most popular position each state 

    # def mapoper_position_experience_count(self,position,experience):
    #     yield ()

    def combiner_count_state_to_position(self, state, position_count):
        # sum the positions counts for every state in every mapper
        position_sum = 0
        for position, count in position_count:
            position_sum += count  
            yield (state, (position,position_sum))

    def reducer_count_position_to_state(self, state, position_count):
        # send all (state, (position,position_sum)) pairs to the same reducer to sum on the same state for all the positions.
        # sum the total position counts for every position in every state
        position_sum = 0
        for position, count in position_count:
            position_sum += count  # Accumulate the counts
        yield state, (position_sum, position)

    def reducer_find_max_position_in_every_state(self, state, postoexp_count_pairs):
        #calculate the max position sum between all positions in all states
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
            MRStep(mapper=self.mapper_state_to_position,
                   combiner=self.combiner_count_state_to_position,
                   reducer=self.reducer_count_position_to_state),
            MRStep(reducer=self.reducer_find_max_position_in_every_state)
        ]


if __name__ == '__main__':
    MRStateToPosition.run()
    
    # file_ = open("C:/Users/Habiba ElHussieny/Downloads/Big Data/Project/career_nav/Map-Reduce/state-position_output.txt", "w")
    # subprocess.Popen("ls", stdout=file_)