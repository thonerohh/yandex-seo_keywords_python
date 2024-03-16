# load output1-0.csv and return only unique values in "Query" column and save the result to output1-1.csv

import pandas as pd

# Load the combined CSV file
combined_df = pd.read_csv('output1-0-1.csv')

# Drop duplicates from the "Query" column
unique_df = combined_df.drop_duplicates(subset='Query')

# Save the unique data to a new CSV file
unique_df.to_csv('output1-1-1.csv', index=False)