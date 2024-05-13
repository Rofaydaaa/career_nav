from mrjob.job import MRJob
from mrjob.step import MRStep
from operator import itemgetter

class MRMostPostings(MRJob):

    def mapper_postings(self, _, line):
        line_cols = line.split(',') 
        yield line_cols[13], 1  # yielding the column chosen, here we are choosing the field orgCompany_nameOrg (13)

    def combiner_sum_positings_per_org(self, orgName, count):
        # sum the positions counts for every organization in every mapper
        # print(orgName, sum(count))
        yield orgName, sum(count)

    def reducer_global_sum_positings_per_org(self, orgName, count):
        total_count = sum(count)
        yield None, (orgName, total_count)

    def reducer_most_postings(self, _, orgName_totalCount_pair):
        sorted_state_counts = sorted(orgName_totalCount_pair, key=itemgetter(1), reverse=True)
        for state, count in sorted_state_counts:
            yield state, count

    def steps(self):
        return [
            MRStep(mapper=self.mapper_postings,
                   combiner=self.combiner_sum_positings_per_org,
                   reducer=self.reducer_global_sum_positings_per_org),
            MRStep(reducer=self.reducer_most_postings)
        ]

if __name__ == '__main__':
    MRMostPostings.run()