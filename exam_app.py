import streamlit as st
import pandas as pd

def main():
    # Set up the app layout
    st.title('Google Sheets-like Web Page')

    # Create an empty dataframe to store the data
    data = pd.DataFrame()

    # Add a button to add a new row
    if st.button('Add Row'):
        data = add_row(data)

    # Display the data table
    if not data.empty:
        st.dataframe(data)

def add_row(data):
    # Get user input for each column
    name = st.text_input('Name')
    age = st.number_input('Age')
    email = st.text_input('Email')

    # Add the row to the dataframe
    new_row = pd.DataFrame([[name, age, email]], columns=['Name', 'Age', 'Email'])
    data = data.append(new_row, ignore_index=True)

    return data

if __name__ == '__main__':
    main()
