import csv
import os

def csv_to_text(csv_file, text_file):
    with open("./CSVs/"+csv_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        with open("./Map-Reduce/"+text_file, 'w') as text_file:
            for row in csv_reader:
                text_file.write('¶'.join(row) + '\n')

csv_to_text('final_output_processed_70k.csv', 'output.txt')
