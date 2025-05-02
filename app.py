import streamlit as st
import generation

# Title of the chatbot UI
st.title("Suvidha")

# Instructions
st.write("Welcome to Suvidha! Please select the domain and type your query below.")

# Dropdown to select domain
domain = st.selectbox(
    "Select the domain of your query:",
    ["Banking", "E-Commerce", "Medical"]
)

# Create an input box for user to type their query
user_input = st.text_input("Please enter your Query:")

# Display a response once the user enters a query
if user_input:
    # Pass both domain and user input to the response generator
    response = generation.generate_response(domain,user_input)
    
    # Display the response
    st.write(response)
