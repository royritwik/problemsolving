import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st
import snowflake.connector

# Connect to Snowflake
conn = snowflake.connector.connect(
    user='<YOUR_USERNAME>',
    password='<YOUR_PASSWORD>',
    account='<YOUR_ACCOUNT_URL>',
    warehouse='<YOUR_WAREHOUSE>',
    database='<YOUR_DATABASE>',
    schema='<YOUR_SCHEMA>'
)

# Load the questions from Snowflake
def load_questions(num_questions):
    query = f"SELECT * FROM questions LIMIT {num_questions}"
    cursor = conn.cursor()
    cursor.execute(query)
    questions = cursor.fetchall()
    return questions

# Validate the answers
def validate_answers(answers):
    query = f"SELECT * FROM questions"
    cursor = conn.cursor()
    cursor.execute(query)
    questions = cursor.fetchall()
    correct_count = sum(answers == row[5] for row in questions)
    return correct_count

# Main function
def main():
    # Set up the app layout
    st.title('MCQ Questions')
    num_questions = st.slider('Select the number of questions to display', min_value=1, max_value=100, value=10)
    questions = load_questions(num_questions)

    # Display the questions and collect user answers
    answers = []
    for idx, row in enumerate(questions):
        st.subheader(f'Question {idx+1}: {row[1]}')
        options = [row[2], row[3], row[4], row[5]]
        selected_option = st.selectbox('Select your answer:', options)
        answers.append(selected_option)

    # Validate the answers
    correct_count = validate_answers(answers)

    # Display the result
    st.subheader('Result')
    st.write(f'Correct answers: {correct_count} out of {num_questions}')

if __name__ == '__main__':
    main()
