import streamlit as st 

st.header("Contact Me")

with st.form(key="my_form"):
    user_email = st.text_input("Your Email Address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        print("Submitted")



        message = message + user_email






