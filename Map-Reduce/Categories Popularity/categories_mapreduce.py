from mrjob.job import MRJob
from mrjob.step import MRStep

class MRCategories(MRJob):

    def mapper_get_categories(self, _, line):
        line_cols = line.split('¶')  # splitting the line into each field by the delimitter that I have added while generating the txt file 
        yield (line_cols[0], 1)  #yielding the column chosen, here we are choosing the field orgTags_CATEGORIES to find the popularity of each category

    def combiner_count_categories(self, category, counts):
        # sum the categories we've seen so far
        yield (category, sum(counts))

    def reducer_count_categories(self, category, counts):
        # send all (counts,category) pairs to the same reducer.
        yield None,(sum(counts),category)

    # discard the key; it is just None
    def reducer_sorted_categories(self, _, category_count_pairs):
        # each item of category_count_pairs is (count, category),
        # so yielding for every category its count but after sorting
        try:
            for count, category in sorted(category_count_pairs, reverse=True):
                yield (category,count)
        except ValueError:
            pass

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_categories,
                   combiner=self.combiner_count_categories,
                   reducer=self.reducer_count_categories),
            MRStep(reducer=self.reducer_sorted_categories)
        ]


if __name__ == '__main__':
    MRCategories.run()
