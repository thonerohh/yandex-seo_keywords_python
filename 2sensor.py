# load output 1-1.csv and drop 2+ columns and pass further

import pandas as pd
from datetime import datetime

def count_days(start_date_str, end_date_str):
    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(start_date_str, date_format)
    end_date = datetime.strptime(end_date_str, date_format)
    delta = end_date - start_date
    return delta.days

# Load the combined CSV file
combined_df = pd.read_csv('output1-1-1.csv')
main_columns = ['Query','Dates range', 'Avg. position']

# drop everything further from first 2 columns from combined_df
combined_df = combined_df[main_columns]

# create new pandas dataframe with 2 columns
df = pd.DataFrame(columns=main_columns)

# first column is query length
df[main_columns[0]] = combined_df[main_columns[0]].apply(lambda x: len(x))

# second column is to count days between start date and end date format example is "YYYY-MM-DD - YYYY-MM-DD"
df[main_columns[1]] = combined_df[main_columns[1]].apply(lambda x: count_days(x.split(' - ')[0], x.split(' - ')[1]))

# third column just copy from combined_df
df[main_columns[2]] = combined_df[main_columns[2]]

# add forth column with default query
df['Default query'] = combined_df['Query']

# Save the unique data to a new CSV file
df.to_csv('output2-1-0-1.csv', index=False)