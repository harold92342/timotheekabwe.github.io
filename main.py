import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Timothée Kabwe")
    content= """
    Hi, I am Timothy Kabwe! I am an IT Support Technician at Kamoa Copper SA(Ivanhoe Mines Group) and also i am a 
    Data Analyst enthusiast.  
    """
    st.info(content)