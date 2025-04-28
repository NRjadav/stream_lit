# app.py
import streamlit as st

st.title('Hello Streamlitok!')
st.write('Welcome to your first Streamlit app.')

name = st.text_input('Enter your name:')
if name:
    st.success(f'Hello, {name}! Welcome to the app.')
