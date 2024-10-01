import streamlit as st
from PIL import Image

# --- LOAD ASSETS
fig1 = Image.open('images/placeholder.png')
# img_name = Image.open('images/name.png')


# --- HEADER
with st.container():
    st.title('Source Code')

with st.container():
    st.header('Prerequisite Code')
    st.image(fig1)
