import streamlit as st
from PIL import Image

# To test: streamlit run Home.py
# To deploy: git add .
# git commit -m "message"
# git push heroku main
# (git push -u origin main)

# Emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title='Colin McCann - Projects', page_icon=':desktop_computer:', layout='wide')

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load Assets
fig1 = Image.open('images/placeholder.png')
flight_destination_fig = Image.open('images/AirportFig1.png')
day_of_week_fig = Image.open('images/AirportFig2.png')
stock_fig = Image.open('images/stockgraph.png')
minecomputer_fig = Image.open('images/FullAdder.png')
# fig4 = Image.open('images/name.png')


# === Header ===
with st.container():
    st.title('Colin McCann - Projects')
    st.write('Math/statistics Major at Binghamton University')
    st.markdown('[LinkedIn](https://www.linkedin.com/in/cmccann2)')
    st.markdown('[Github](https://github.com/CMcCann44)')


# === Projects ===
# --- JFK Flight Data Analysis ---
with st.container():
    st.write('---')
    text_column, image_column = st.columns(2)
    with text_column:
        st.subheader('Airport Flight Data Analysis')
        st.write('Used Pandas to analyze large JFK airport datasets with >25,000 entries and determine possible causes of flight delays.')
        st.write('Performed chi-square and t-tests to determine if certain factors were significantly correlated with flight delay, '
                 'such as day of the week, flight destination (graph shown on right), airline, etc.')
    with image_column:
        st.image(flight_destination_fig)

# --- Stock Market Web Scraping ---
with st.container():
    text_column, image_column = st.columns(2)
    with text_column:
        st.subheader('Stock Market Web Scraping')
        st.write('Used yFinance and BeautifulSoup to scrape and parse web stock data.')
        st.write('Also used Pandas and Plotly to create graphs showing stock trends.')
    with image_column:
        st.image(stock_fig)

# --- Minecraft Computer ---
with st.container():
    text_column, image_column = st.columns(2)
    with text_column:
        st.subheader('Minecraft Computer')
        st.write('Built original adder (shown on right) and register using in-game wiring system.')
        st.write('Working on an original 8-bit CPU.')
    with image_column:
        st.image(minecomputer_fig)

# --- Classification Machine Learning ---
with st.container():
    st.subheader('Recodings for Classification Machine Learning Models (Current)')
    st.write('As part of research projects with Dr. Singh and Dr. Kurtz at Binghamton University.')
#    st.write('Working on an ellipse-based recoding method and a pairwise relational feature recoding.')


# --- Probability Distribution Generator ---



# === Education ===
# --- College ---
with st.container():
    st.write('---')
    st.header('College')
    st.write('Math/data science major and CS minor at Binghamton University')
    st.subheader('Courses Taken')
    st.write('Calculus I-III, Linear Algebra, Number Systems, '
            'Programming and Hardware Fundamentals, Probability Theory, ')
            # 'Advanced Linear Algebra, Mathematical Statistics')
            # 'Real Analysis, Regression Models, Computing')

# --- Coursera ---
with st.container():
    st.write('---')
    st.header('Coursera')
    st.write('Learned Python for data science through 5 courses. Certificates shown on LinkedIn.')

# === Footer ===
with st.container():
    st.write('---')
    st.write('Website created using Streamlit in Python.')
    st.write('Deployed 10/23/24. Last updated 10/23/24.')
    st.markdown('[How I learned StreamLit -->](https://www.youtube.com/watch?v=VqgUkExPvLY)')
