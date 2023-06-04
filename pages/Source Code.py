import streamlit as st
from PIL import Image

# --- LOAD ASSETS
prereqs = Image.open('images/prereqs.png')
header = Image.open('images/header.png')
research1 = Image.open('images/research1.png')
research2 = Image.open('images/research2.png')
airport1 = Image.open('images/airport1.png')
airport2 = Image.open('images/airport2.png')
college = Image.open('images/college.png')
# img_name = Image.open('images/name.png')


# --- HEADER
with st.container():
    st.title('Source Code')

with st.container():
    st.header('"Prerequisite Code"')
    st.image(prereqs)

with st.container():
    st.header('Header')
    st.image(header)

with st.container():
    st.header('Research')
    st.image(research1)

with st.container():
    st.header('Research (cont)')
    st.image(research2)

with st.container():
    st.header('WISE Airport')
    st.image(airport1)

with st.container():
    st.header('WISE Airport (cont)')
    st.image(airport2)

with st.container():
    st.header('College/Future Plans')
    st.image(college)
