import streamlit as st
from PIL import Image

st.set_page_config(page_title='More', page_icon=':desktop_computer:', layout='wide')

# --- LOAD ASSETS
fig1 = Image.open('images/placeholder.png')
full_adder_fig = Image.open('images/FullAdder.png')
mux_fig = Image.open('images/Mux.png')
# sr_latch_fig = Image.open('images/SRLatch.png')
# register_fig = Image.open('images/Register.png')
# img_name = Image.open('images/name.png')


# --- HEADER
with st.container():
    st.title('More Detail on Current Projects')
    st.header('Minecraft Computer')

with st.container():
    text_column1, text_column2 = st.columns(2)
    with text_column1:
        st.subheader('Original Full Adder')
        st.image(full_adder_fig)
    with text_column2:
        st.subheader('Original Multiplexer')
        st.image(mux_fig)

with st.container():
    st.header('Machine Learning Classification Models')
    st.write('More info to come')
