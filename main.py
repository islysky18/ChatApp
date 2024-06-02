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

def main():
    # Set title of the app
    st.title("Echo Bot")

    # Get user input
    user_input = get_user_input()
    if st.button("Send"):
        if user_input:
            display_output(user_input)
            clear_input()


def get_user_input():
    user_text = st.text_input("You:", "")
    return user_text

def display_output(user_input):
    st.text(f"Echo: {user_input}")

def clear_input():
    st.text_input("You:", "", key="clear")

if __name__ == "__main__":
    main()