# load input.csv and parse column "Query" then remove lines with "bt-technika" and save the result to output1.csv

import csv
import os
input_file = 'input3.csv'
output_file = 'output13.csv'

if not os.path.exists(input_file):
  print(f"Error: {input_file} does not exist.")
else:
  with open(input_file, 'r', encoding='utf-8', newline='') as inp, open(output_file, 'w', encoding='utf-8', newline='') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
      if 'bt-technika' not in row[0]:
        writer.writerow(row)
