import streamlit as st 
from send_email import send_email

st.header("Contact Me")

with st.form(key="my_form"):
    user_email = st.text_input("Your Email Address")
    new_message = st.text_area("Your message")
    message = f"""\
        Subject: New Mail from {user_email}
        From: {user_email}
        {new_message}
        """
    
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your Email was sent successfully!")
        









