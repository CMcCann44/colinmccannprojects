import streamlit as st
from PIL import Image

# streamlit run Home.py
# Emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title='Colin McCann', page_icon=':desktop_computer:', layout='wide')


# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Load Assets
fig1 = Image.open('images/placeholder.png')
# fig2 = Image.open('images/name.png')
# fig3 = Image.open('images/name.png')


# === HEADER ===
with st.container():
    st.title('Colin McCann')
    st.subheader('Updated 09/17/24')
    st.write('Website created using Streamlit (Python library).')


# === Projects ===
# --- Website ---
with st.container():
    image_column, text_column = st.columns(2)
    with image_column:
        st.image(fig1)
    with text_column:
        st.subheader('Build a Website in only 12 minutes using Python & Streamlit')
        st.write('Learned how to use StreamLit.')
        st.markdown('[Full Video -->](https://www.youtube.com/watch?v=VqgUkExPvLY)')
        st.image(fig1)


# --- JFK Flight Data Analysis ---
with st.container():
    text_column, image_column = st.columns(2)
    with text_column:
        st.subheader('JFK Flight Data Analysis')
        st.write('##')
        st.write('Used Pandas to analyze large airport datasets and determine possible causes of flight delays.')
    with image_column:
        st.image(fig1)

with st.container():
    text_column, image_column = st.columns(2)
    with text_column:
        st.write('Performed chi-square and __ tests '
                 'to determine if certain factors were significantly correlated with flight delay.')
    with image_column:
        st.image(fig1)


# --- Stock Market Web Scraping ---



# === IN PROGRESS ===
# --- Minecraft Computer ---
with st.container():
    text_column, image_column = st.columns(2)
    with text_column:
        st.subheader('JFK Flight Data Analysis')
        st.write('##')
        st.write('Analyzed large airport datasets to determine possible causes of flight delays.')
    with image_column:
        st.image(fig1)

with st.container():
    text_column, image_column = st.columns(2)
    with text_column:
        st.write('Used the Pandas library in Python to perform chi-square and __ tests '
                 'to determine if any factors were significantly correlated with flight delay.')
    with image_column:
        st.image(fig1)

# --- Probability Distribution Generator ---


# === BU ===
# --- College ---
with st.container():
    st.write('---')
    st.header('College')
    image_column, text_column = st.columns(2)
    with image_column:
        st.image(fig1)
    with text_column:
        st.write('Math major, CS minor.')
        st.write('Courses taken: Calculus I-III, Linear Algebra, Number Systems, Probability Theory, '
                 'Mathematical Statistics, Programming and Hardware Fundamentals')

# --- Coursera ---
with st.container():
    st.write('---')
    st.header('Past Projects')
    st.write('##')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(fig1)
    with text_column:
        st.subheader('')
        st.write('Learned the basics of Python.')
        st.markdown('[Full Video -->](https://www.youtube.com/watch?v=_uQrJ0TkZlc)')
