import streamlit as st

# Hide MainMenu, Header (with GitHub icon), Footer
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    #header {visibility: hidden;}
    #footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Your App Content
st.title('Hello Streamlit!')
st.write('Welcome to your first Streamlit app.')

name = st.text_input('Enter your name:')
if name:
    st.success(f'Hello, {name}! Welcome to the app.')
