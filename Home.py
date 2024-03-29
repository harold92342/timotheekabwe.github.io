import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Timothée Kabwe")
    content= """
    Hi, I am Timothy Kabwe a Dedicated IT Support Technician with a proven track record in
    network operations,troubleshooting, and comprehensive printer support. Additionally, bring expertise in data analysis, navigating complex
    datasets, and contributing valuable insights for informed decision-making.  
    """
    st.info(content)
content2="""
"Below you can find some of the apps I have built in Python. Feel free to contact me!"
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")