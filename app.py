from dotenv import load_dotenv
load_dotenv() ## load all environment variables
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

## Configure API key
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

## Function to Load Google Gemini Model and provide sql query as response

def get_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text 


## Function to retrieve query from the sql database
def read_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define prompt
prompt = [ """ You are an expert in converting English questions to SQL queries!
The SQL database has the name sakilav2 and has the following table film with columns - filmID,
title, description, releaseYear, length, replacementCost, rating.

For example, 
Example 1 - Show the title and the replacement cost for films with a replacement 
cost of more than 28.00. The SQL command will be something like this: 
SELECT title, replacementCost FROM film WHERE replacementCost > 28.00;

Example 2 - Show the title, description, rating, and length of films that have a length of 120. 
The SQL command will be something like: 
SELECT title, description, rating, length FROM film WHERE length = 120;

Example 3 - Retrieve all films released in 2010. 
The SQL command will be something like: 
SELECT * FROM film WHERE releaseYear = 2010;

Example 4 - Get all films ordered by length in descending order. 
The SQL command will be something like: 
SELECT * FROM film ORDER BY length DESC;

Example 5 - Count the number of films for each rating. 
The SQL command will be something like: 
SELECT rating, COUNT(*) AS film_count FROM film GROUP BY rating;

Example 6 - Find the longest film. 
The SQL command will be something like: 
SELECT * FROM film ORDER BY length DESC LIMIT 1;

Example 7 - Find films that do not have a description. 
The SQL command will be something like: 
SELECT * FROM film WHERE description IS NULL;

Example 8 - Get films that contain the word "CAT" in their title. 
The SQL command will be something like: 
SELECT * FROM film WHERE title LIKE '%CAT%';

Example 9 - Update the rating of a specific film to 'PG-13'. 
The SQL command will be something like: 
UPDATE film SET rating = 'PG-13' WHERE title = 'A FAIR RACE';

Example 10 - Delete a film from the database. 
The SQL command will be something like: 
DELETE FROM film WHERE filmID = 5;

The SQL code should not have ``` in the beginning or end and the word 'SQL' should not appear in the output."""]

# import streamlit as st
import sqlite3

def read_query(sql_query, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(sql_query)
    
    # Fetch column names
    column_names = [description[0] for description in cursor.description]
    
    # Fetch data
    data = cursor.fetchall()
    
    conn.close()
    
    return column_names, data


import pandas as pd

# Streamlit App Configuration
st.set_page_config(page_title="SQL Query Generator", layout="centered", page_icon=":bar_chart:")

# App Title and Description
st.title("GEMINI SQL Query Generator")
st.write("Enter your query description below to generate and execute an SQL query.")

# Input form for the query description
query_description = st.text_input("Describe your query:", key="input")
submit = st.button("Generate and Run Query")

# If 'Submit' is clicked
if submit:
    # Generate SQL query from text description
    sql_query = get_response(query_description, prompt)  # Replace with your function to generate SQL
    st.write(f"**Generated SQL Query:**")
    st.code(sql_query)  # Display the generated SQL query
    
    # Execute the generated SQL query and fetch data
    column_names, data = read_query(sql_query, "film.db")  # Updated to fetch column names and data
    
    # Check if data is not empty and construct DataFrame
    if data:
        df = pd.DataFrame(data, columns=column_names)
        
        st.success(f"Query executed successfully! Returned {len(df)} rows.")
        st.write("### Query Results:")
        
        # Display results in a table format
        st.dataframe(df)  # Displaying data in a DataFrame table
        
    else:
        st.warning("No data returned from the query, or the query might be invalid.")
