import streamlit as st
import pandas as pd
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('survey.db')

# Create the survey table if it doesn't exist
create_table_query = '''
    CREATE TABLE IF NOT EXISTS survey (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        response TEXT
    )
'''
conn.execute(create_table_query)

# Load the questions from the database
def load_questions():
    query = "SELECT question FROM survey"
    cursor = conn.cursor()
    cursor.execute(query)
    questions = [row[0] for row in cursor.fetchall()]
    return questions

# Main function
def main():
    # Set up the app layout
    st.title('Survey Form')

    # Load the questions
    questions = load_questions()

    # Display the form
    with st.form(key='survey_form'):
        for idx, question in enumerate(questions):
            st.subheader(f'Question {idx+1}:')
            st.write(question)
            response = st.text_input(f'Response to Question {idx+1}')
            st.write('---')

        submitted = st.form_submit_button(label='Submit')

        if submitted:
            # Store the responses in the database
            with conn:
                for idx, question in enumerate(questions):
                    response = st.session_state[f'response to question {idx+1}']
                    conn.execute("INSERT INTO survey (question, response) VALUES (?, ?)", (question, response))

            # Display a success message
            st.success('Survey submitted successfully!')

if __name__ == '__main__':
    main()
