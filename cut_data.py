import os
import pandas as pd


# run this script to split the data into multiple csv files
# The function will read the data from the file Expense_Budget.csv
# and split the data into multiple csv files, one for each unique year
# found in the data. The files will be named <year>_data.csv

def split_csv_by_year(file_path):
    print(f"Reading data from {file_path}")
    df = pd.read_csv(file_path)
    unique_years = df['Fiscal Year'].unique()

    print(f"Found {len(unique_years)} unique years in the data")
    for year in unique_years:
        df_year = df[df['Fiscal Year'] == year]
        df_year.to_csv(f'{year}_data.csv', index=False)
        print(f"Saved data for year {year} to {year}_data.csv")

# Print the current working directory
print(f"Current working directory: {os.getcwd()}")

# Print all files in the current working directory
print("Files in current working directory:")
for file in os.listdir():
    print(file)

split_csv_by_year('Expense_Budget.csv')
