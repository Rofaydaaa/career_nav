import csv
import os
import pandas as pd

def csv_to_text(csv_file, text_file):
    # with open(csv_file, 'r') as csv_file:
    #     csv_reader = csv.reader(csv_file)
    #     with open(text_file, 'a') as text_file:
    #         for row in csv_reader:
    #             text_file.write('¶'.join(row) + '\n')

     with open(text_file, 'a', encoding='utf-8') as output:
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                output.write(','.join(row) + '\n')

csv_to_text('final_output_processed_70k.csv', 'output.txt')

# file_path1 = "C:/Users/Habiba ElHussieny/Downloads/Big Data/Project/career_nav/CSVs/final_output_processed_70k.csv"
# file_path2 = "C:/Users/Habiba ElHussieny/Downloads/Big Data/Project/career_nav/CSVs/final_output_processed_33k.csv"

# # Read the first CSV file into a Pandas DataFrame
# df1 = pd.read_csv(file_path1)
# df1 = df1[df1['orgTags_CATEGORIES'] != 'NOT FOUND']  # Remove rows where 'orgTags_SKILLS' is 'NOT FOUND'

# # Read the second CSV file into another Pandas DataFrame
# df2 = pd.read_csv(file_path2)
# df2 = df2[df2['orgTags_CATEGORIES'] != 'NOT FOUND']  # Remove rows where 'orgTags_SKILLS' is 'NOT FOUND'

# # Concatenate the two DataFrames into a single DataFrame
# df_jobs = pd.concat([df1, df2], ignore_index=True)

# df_jobs

# n = len(pd.unique(df_jobs['orgTags_CATEGORIES']))
 
# print("No.of.unique values :", 
#       n)

# df_jobs.to_csv("C:/Users/Habiba ElHussieny/Downloads/Big Data/Project/career_nav/CSVs/filtered_categories.csv",index=False)
