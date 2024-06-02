import os
from dotenv import load_dotenv
import openai
import requests
import json

import time
import logging
from datetime import datetime
import streamlit as st

load_dotenv()

client = openai.OpenAI()

model = "gpt-4o"

# st.title("Echo Bot")

# # Create a text input for the user to type their message
# user_input = st.text_input("You", "")

# # Create a button that user can click to submit their message
# if st.button("Send"):
#     st.text(f"Echo: {user_input}")

# def main():
#     # Set title of the app
#     st.title("Echo Bot")

#     # Get user input
#     user_input = get_user_input()
#     if st.button("Send"):
#         if user_input:
#             display_output(user_input)
#             clear_input()


# def get_user_input():
#     user_text = st.text_input("You:", "")
#     return user_text

# def display_output(user_input):
#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     st.text(f"Echo {current_time}: {user_input}")

# def clear_input():
#     st.text_input("You:", "", key="clear")

# if __name__ == "__main__":
#     main()

# ==================================================
# persist the session state

def main():
    st.title("Echo Bot")

    history = []
    # initialize session state for the input field if not already done
    if 'input' not in st.session_state:
        st.session_state.input = ""
    
    if 'history' not in st.session_state:
        st.session_state.history = []

    # Create a form for user input to ensure the input field can be clear
    with st.form(key='input_form', clear_on_submit=True):
        user_input = st.text_input("You:", st.session_state.input)
        submit_button = st.form_submit_button(label="Send")
        

    if submit_button:
        if user_input:

            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            st.session_state.history.append(f"User ({current_time}): {user_input}")
            bot_response = f"Bot ({current_time}): {user_input}"
            st.session_state.history.append(bot_response)

            # clear the user input
            st.session_state.input = ""
            display_output(user_input)

    st.subheader("Conversation history:")
    for message in st.session_state.history:
        st.text(message)

def display_output(user_input):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.text(f"Echo {current_time}: {user_input}")
    


if __name__ == "__main__":
    main()