import streamlit as st 
from send_email import send_email

st.header("Contact Me")


with st.form(key="my_form"):
    user_email = st.text_input("Your Email Address")
    new_message = st.text_area("Your message")

    full_message = new_message + "\n\n" + f"From: {user_email}"
    message = "Subject: New Mail from Project Showcase App\n\n" + full_message 

    button = st.form_submit_button("Submit")
    if button:
        try:
            send_email(message)
            st.info("Your Email was sent successfully!")
        except Exception as e:
            st.error(f"Error: {e} Your message was not sent properly")            
    









