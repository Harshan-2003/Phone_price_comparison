import streamlit as st
#from streamlit_option_menu import option_menu
#from PIL import Image
st.set_page_config(page_title="sap_ondc",page_icon=":telephone:",layout="wide")
with st.container():
    st.markdown("<h1 style='text align:center;color:green;'>WELCOME !!!</h1>",unsafe_allow_html=True)
with st.container():
    st.markdown("<h2 style='text align:center;color:green;'>Explore the dream world of gadgets in a single site!!</h1>", unsafe_allow_html=True)
    st.image("images1.jpg")
    st.markdown("<h3 style='text align:center;color:green;'>Let's get started.....</h3>", unsafe_allow_html=True)
st.sidebar.success("select pages above")
with st.container():
    st.markdown("<h3 style='text align:center;color:green;'>For more searches refer to search tab</h3>",unsafe_allow_html=True)









