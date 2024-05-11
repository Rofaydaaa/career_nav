from mrjob.job import MRJob
from mrjob.step import MRStep

class MRCompaniesWithMostJobPostings(MRJob):

    def mapper_get_companies(self, _, line):
        line_cols = line.split('¶')  # splitting the line into each field by the delimitter that I have added while generating the txt file 
        yield (line_cols[15], 1)  #yielding the column chosen, here we are choosing the field orgCompany_nameOrg to find the most mentioned organization 

    def combiner_count_companies(self, company, counts):
        # sum the companies we've seen so far
        yield (company, sum(counts))

    def reducer_count_companies(self, company, counts):
        # send all (num_occurrences, company) pairs to the same reducer.
        # num_occurrences is so we can easily use Python's max() function.
        yield None, (sum(counts), company)

    # discard the key; it is just None
    def reducer_find_max_company(self, _, company_count_pairs):
        # each item of company_count_pairs is (count, company),
        # so yielding one results in key=counts, value=company
        try:
            yield max(company_count_pairs)
        except ValueError:
            pass

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_companies,
                   combiner=self.combiner_count_companies,
                   reducer=self.reducer_count_companies),
            MRStep(reducer=self.reducer_find_max_company)
        ]


if __name__ == '__main__':
    MRCompaniesWithMostJobPostings.run()
