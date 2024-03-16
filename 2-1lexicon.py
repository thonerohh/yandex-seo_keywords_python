# load output2-2.csv and remove all lines where "Default query" contains some a-Z characters

import pandas as pd
import os
import regex as re

# Load the combined CSV file
combined_df = pd.read_csv('output2-2.csv')

# Remove all lines where "Default query" contains some a-Z characters
combined_df = combined_df[combined_df['Default query'].str.contains(r'[a-zA-Z]') == False]

# Save the unique data to a new CSV file

combined_df.to_csv('output2-3.csv', index=False)