import streamlit as st


st.header("Login Form")
st.subheader("Please enter your credentials to login")
with st.form(key='login_form'):
    username=st.text_input("Enter your username:",key="username_input")
    password=st.text_input("Enter your password:",type="password",key="password_input")
    login_button=st.form_submit_button(label="Login")