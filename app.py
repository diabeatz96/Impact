import sys
import streamlit as st
import pandas as pd

def main():
    chunksize = 10 ** 5 # 100,000 rows at a time
    pr = None
    data = None
    
    
    data_types = {
    "Publication Date": "str",
    "Fiscal Year": "int64",
    "Agency Number": "str",
    "Agency Name": "str",
    "Unit Appropriation Number": "str",
    "Unit Appropriation Name": "str",
    "Budget Code Number": "str",
    "Budget Code Name": "str",
    "Object Class Number": "str",
    "Object Class Name": "str",
    "Object Code": "str",
    "Object Code Name": "str",
    "Intra-City Purchase Code": "str",
    "Responsibility Center Code": "str",
    "Responsibility Center Name": "str",
    "Personal Service/Other Than Personal Service Indicator": "str",
    "Financial Plan Savings Flag": "str",
    "Adopted Budget Amount": "int64",
    "Current Modified Budget Amount": "int64",
    "Financial Plan Amount": "int64",
    "Adopted Budget Position": "int64",
    "Current Modified Budget Position": "int64",
    "Financial Plan Position": "int64",
    "Adopted Budget - Number of Contracts": "int64",
    "Current Modified Budget - Number of Contracts": "int64",
    "Financial Plan - Number of Contracts": "int64",
}
    
    st.title('Example Data Open NYC Budget Data')
    st.write('Loading 100,000 rows at a time from the NYC Open Budget Data.')
    # Load the CSV data
    try:
        chunksize = 10 ** 5 # 100,000 rows at a time
        data_types = {"column_with_error": "int64"}
        
        ### Load only csv with rows whose year is in 2023 data = data[data['year'] == 2023]
        data = pd.read_csv("data/Expense_Budget.csv", nrows=chunksize, dtype=data_types)
    except ValueError as e:
        # Extract information about the error
        error_message = str(e)
        error_parts = error_message.split("occurred at index ")

        # If the error message contains column and index information
        if len(error_parts) > 1:
            index = int(error_parts[1].split(", ")[0])
            column = error_parts[1].split(", ")[-1].strip()

            print(f"Error occurred at column: {column}, index: {index}")
        else:
            # Handle other types of errors or incomplete information
            print("Error occurred:", error_message)    
        # Show the data
    st.write(data)
  
    st.write('List of all the Agencies')
    st.write(data['Agency Name'].unique())
    
    size = data['Agency Name'].unique().size
    st.write(size)
    edited_df = st.data_editor(data)
    
    
    
    
  
if __name__ == '__main__':
    main()
