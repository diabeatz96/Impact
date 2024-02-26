import sys
import streamlit as st
import pandas as pd

def main():
    chunksize = 10 ** 5 # 100,000 rows at a time
    
    st.title('Example Data Open NYC Budget Data')
    st.write('Loading 100,000 rows at a time from the NYC Open Budget Data.')
    # Load the CSV data
    data = pd.read_csv('data/Expense_Budget.csv', nrows=chunksize)
    
    # Show the data
    st.write(data)
  
if __name__ == '__main__':
    main()
