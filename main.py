import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=300)
    
with col2:
    st.title("Jeremy Abraham")
    
    content = """Hello im Jeremy a junior Python Developer and Data Engineer. I specialize in harnessing data to drive significant business improvements and elevate customer experiences. With attention to detail, I transform intricate data into actionable solutions and insights. My technical prowess spans Python, SQL, Java, Excel, Tableau and advanced analytics, enabling businesses to make data informed decisions swiftly and effectively."""
    
    st.info(content)

content2 = """Below you can find some of the apps i have built in Python. Feel free to contact me!"""

st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])


df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+ row["image"])
        st.write("[Source Code](https://github.com/Wiinds)")
        #for dynamic weblink for each project instead of a static one
        #st.write(f"[Source Code]({row['url']})")
        
        
    
    
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+ row["image"])
        st.write("[Source Code](https://github.com/Wiinds)")
        
        
        
   








