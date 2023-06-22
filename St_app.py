import streamlit as st
from PIL import Image

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

st.write("Welcome to My Page")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Yassine BENKADDOUR :wave:")
    st.title("A Data Analyst From Nuitee")
    st.write(
        "I am passionate BA about finding ways to use Python and VBA to be more efficient and effective in business settings."
    )
    st.write("[Yassine Portfolio >](https://pythonandvba.com)")
    
    
#insert image
Yassine_image= Image.open("C:/Users/My PC/Desktop/Python file Yas/X Steamlit/BA2.png") 
Nt=Image.open("C:/Users/My PC/Desktop/Python file Yas/X Steamlit/NT-logo.png")
st.image(Nt)
st.image(Yassine_image)


