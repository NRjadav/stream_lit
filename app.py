import streamlit as st

# Hide MainMenu, Header, Footer and "Manage App" button
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    section[data-testid="stSidebar"] {visibility: hidden;}  /* (optional: sidebar if needed) */
    .st-emotion-cache-zq5wmm {display: none;} /* hide manage app button */
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Your App Content
st.title('Hello Streamlit!')
st.write('Welcome to your first Streamlit app.')

name = st.text_input('Enter your name:')
if name:
    st.success(f'Hello, {name}! Welcome to the app.')
