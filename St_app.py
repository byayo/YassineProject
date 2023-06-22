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
    st.write("[Yassine Portfolio >](https://yassine.com)")
    
    
#insert image
#Yassine_image= Image.open("C:/Users/My PC/Desktop/Python file Yas/X Steamlit/BA.jpg") 
image2="https://i.pcmag.com/imagery/articles/02Xkt5sp3fVl5rGUtk3DXMi-7.fit_lim.size_1600x900.v1569485349.jpg"
#Nt=Image.open("C:/Users/My PC/Desktop/Python file Yas/X Steamlit/NT-logo.png")
NT2="https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_170,w_170,f_auto,b_white,q_auto:eco,dpr_1/ixhpra0whi6jmwut52vf"
st.image(NT2)
st.image(image2)


