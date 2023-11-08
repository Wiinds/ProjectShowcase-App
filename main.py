import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=600)
    
with col2:
    st.title("Jeremy Abraham")
    content = """Hello im Jeremy a junior Python Developer and Data Engineer"""
    st.info(content)

content2 = """Below you can find some of the apps i have built in Python. Feel free to contact me!"""

st.write(content2)

col3, col4 = st.columns(2)


df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
    
    
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
   








