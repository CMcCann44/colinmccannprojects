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


# === Header ===
with st.container():
    st.title('Colin McCann - Projects')
    st.write('Data Science Major at Binghamton University')
    text_column1, text_column2 = st.columns(2)
    with text_column1:
        st.markdown('[LinkedIn](https://www.linkedin.com/in/colin-mccann-1979922a3/)')
    with text_column1:
        st.markdown('[Github](https://github.com/CMcCann44)')


# === Projects ===
# --- JFK Flight Data Analysis ---
with st.container():
    st.write('---')
    text_column, image_column = st.columns(2)
    with text_column:
        st.subheader('Airport Flight Data Analysis')
        st.write('Used Pandas to analyze large JFK airport datasets with >100,000 entries and determine possible causes of flight delays.')
        st.write('Performed chi-square and t-tests to determine if certain factors were significantly correlated with flight delay, '
                 'such as day of the week, flight destination, airline, etc.')
    with image_column:
        st.image(fig1)

# --- Stock Market Web Scraping ---
with st.container():
    text_column, image_column = st.columns(2)
    with text_column:
        st.subheader('Stock Market Web Scraping')
        st.write('Used yFinance and BeautifulSoup to scrape and parse web stock data. '
                 'Also used Pandas and Plotly to create graphs showing stock trends.')
    with image_column:
        st.image(fig1)

# --- Minecraft Computer ---
with st.container():
    text_column, image_column = st.columns(2)
    with text_column:
        st.subheader('Minecraft Computer')
        st.write('Built original design for a 4-bit adder and register using in-game wiring system. Working on an original 16-bit CPU.')
    with image_column:
        st.image(fig1)

# --- Ellipsoid Recoding for Classification Machine Learning ---
with st.container():
    text_column, image_column = st.columns(2)
    with text_column:
        st.subheader('Ellipsoid Recoding for Classification Machine Learning Models (current)')
        st.write('As part of research projects with Dr. Singh and Dr. Kurtz at Binghamton University. '
                 'Working on an ellipse-based recoding method and a pairwise relational feature recoding.')
    with image_column:
        st.image(fig1)


# --- Probability Distribution Generator ---


# === BU ===
# --- College ---
with st.container():
    st.write('---')
    st.header('College')
    st.write('Math/data science major, CS minor at Binghamton University')
    st.subheader('Courses Taken:')
    st.write('Calculus I-III, Linear Algebra, Number Systems, '
            'Programming and Hardware Fundamentals, Probability Theory')

# --- Coursera ---
with st.container():
    st.write('---')
    st.header('Coursera')
    st.write('Learned Python for data science through 5 courses.')

# === Footer ===
with st.container():
    st.write('---')
    st.write('Deployed 10/01/24. Updated 09/29/24.')
    st.write('Website created using Streamlit in Python.')
    st.markdown('[How I learned StreamLit -->](https://www.youtube.com/watch?v=VqgUkExPvLY)')
