# I have output21+[0-9]\.csv's and I need to find coefficient between "Query" and "Avg. position" columns. I have to use output1-1-1.csv and output2-1-0.csv as input. The result should be saved to output2-2.csv.

import pandas as pd
import os
import regex as re

# Pattern to match the CSV files
pattern = 'output2-1-0-1.csv'
csv_files = [file for file in os.listdir() if re.match(pattern, file)]

# List to hold data from each CSV file
data_frames = []

for filename in csv_files:
    df = pd.read_csv(filename)
    data_frames.append(df)

# Concatenate all the data frames into one
combined_df = pd.concat(data_frames, ignore_index=True)

# If 'Query' column contains numeric values
combined_df = combined_df[(combined_df['Query'] > 21) & (combined_df['Query'] < 44)]

# find median of "Avg. position" column
median = combined_df['Avg. position'].median()

# remove all lines where "Avg. position" is less than median
combined_df = combined_df[combined_df['Avg. position'] > median]

# Save the combined data to a new CSV file
combined_df.to_csv('output2-2.csv', index=False)