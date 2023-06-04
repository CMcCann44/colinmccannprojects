import streamlit as st
from PIL import Image

# streamlit run Home.py
# Emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title='Colin McCann Webpage', page_icon=':desktop_computer:', layout='wide')


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# --- LOAD ASSETS
PythonVideo = Image.open('images/PythonVideo.jpg')
CS50Video = Image.open('images/CS50Video.jpg')
PandasVideo = Image.open('images/PandasVideo.jpg')
StreamlitVideo = Image.open('images/StreamlitVideo.jpg')
img_fig_2 = Image.open('images/Airport Fig2 (Delay vs Day of Week).png')
img_fig_3 = Image.open('images/Airport Fig3 (Delay vs Airline).png')
img_airport_group = Image.open('images/AirportGroup.jpg')
Binghamton = Image.open('images/Binghamton.jpg')
# img_name = Image.open('images/name.png')


# --- HEADER
with st.container():
    st.title('2023 WISE Website')
    st.subheader('Colin McCann')
    st.write('This is my final WISE project created using Python and a coding library called "Streamlit."')
    st.write('I will take you through my different WISE projects, as well as my future plans.')
    st.write('** For a more in-depth look into how this website was made, see the "Source Code" page. '
             'This will show the exact code used to create each section of the main webpage.')


# === PAST ===
# --- Research ---
with st.container():
    st.write('---')
    st.header('Research')
    st.write('##')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(PythonVideo)
    with text_column:
        st.subheader('Python Tutorial - Python Full Course for Beginners')
        st.write('Learned the basics of computer programming as well as many tips and tricks for Python in particular.')
        st.markdown('[Full Video -->](https://www.youtube.com/watch?v=_uQrJ0TkZlc)')

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(CS50Video)
    with text_column:
        st.subheader('Harvard CS50 – Full Computer Science University Course')
        st.write('Learned about how computers actually work, and many problem solving skills.')
        st.markdown('[Full Video -->](https://www.youtube.com/watch?v=8mAITcNt710)')

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(PandasVideo)
    with text_column:
        st.subheader('Complete Python Pandas Data Science Tutorial!...')
        st.write('I used pandas for WISE Airport project - learned how to work with large datasets in Pandas.')
        st.markdown('[Full Video -->](https://www.youtube.com/watch?v=vmEHCJofslg)')

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(StreamlitVideo)
    with text_column:
        st.subheader('Build a Website in only 12 minutes using Python & Streamlit')
        st.write('Learned how to use StreamLit to create this very website you are looking at.')
        st.markdown('[Full Video -->](https://www.youtube.com/watch?v=VqgUkExPvLY)')


# === PRESENT ===
# --- WISE AIRPORT ---
with st.container():
    st.write('---')
    text_column, image_column = st.columns(2)
    with text_column:
        st.header('WISE Airport')
        st.write('##')
        st.subheader('Quarter 3 Group Project:')
        st.write('Jenna Scanlan - Marketing')
        st.write('Kaitlinn Campana - Engineering')
        st.write('Colin McCann - Data Analysis')
    with image_column:
        st.image(img_airport_group)


with st.container():
    text_column, image_column = st.columns(2)
    with text_column:
        st.subheader('Airport Data Analysis')
        st.write('##')
        st.write('My section of the project involved analyzing large datasets of flight data '
                 'to determine possible causes of flight delays.')
    with image_column:
        st.image(img_fig_2)

with st.container():
    text_column, image_column = st.columns(2)
    with text_column:
        st.write('Using a Python library called "pandas" and a excel file thousands of rows '
                 'long that I found online, I could aggregate data into charts and graphs to '
                 'observe any outliers or factors that may be correlated with flight delay.')
    with image_column:
        st.image(img_fig_3)


# === FUTURE ===
# --- College ---
with st.container():
    st.write('---')
    st.header('College/Future Plans')
    image_column, text_column = st.columns(2)
    with image_column:
        st.image(Binghamton)
    with text_column:
        st.write('This fall, I will attend Binghamton University with a major '
                 'in biochemistry and a minor in music.')
        st.write('Although I do not plan to get any degree in computer science, '
                 'I hope to find the time to at least take a few courses to further '
                 'my knowledge in computer science')
