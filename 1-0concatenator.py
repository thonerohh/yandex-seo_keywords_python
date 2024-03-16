# program to combine list of output1\*[0-9]./\.csv to output1.csv where are only similar data in "Query" column

import pandas as pd
import glob
import regex as re

# Pattern to match the CSV files
pattern = 'output1[0-9]+\.csv'
csv_files = [file for file in glob.glob('*.csv') if re.match(pattern, file)]

# List to hold data from each CSV file
data_frames = []

for filename in csv_files:
    df = pd.read_csv(filename)
    data_frames.append(df)

# Concatenate all the data frames into one
combined_df = pd.concat(data_frames, ignore_index=True)

# Optional: Implement any filtering or similarity checks on the "Query" column here
# For now, we'll just keep everything as is.

# Save the combined data to a new CSV file
combined_df.to_csv('output1-0-1.csv', index=False)