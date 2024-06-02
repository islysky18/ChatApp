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

# Set title of the app
st.title("Echo Bot")

# Create a text input for the user to type their message
user_input = st.text_input("You", "")

# Create a button that user can click to submit their message
if st.button("Send"):
    st.text(f"Echo: {user_input}")

