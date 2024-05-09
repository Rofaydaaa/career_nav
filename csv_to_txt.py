import csv

def csv_to_text(csv_file, text_file):
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        with open(text_file, 'w') as text_file:
            for row in csv_reader:
                text_file.write('¶'.join(row) + '\n')

# Example usage
csv_to_text('preprocessing_spark_output2.csv', 'output.txt')
