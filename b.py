import streamlit as st
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="register"   # make sure this database exists
)

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS details (
    NAME VARCHAR(300),
    PASSWORD VARCHAR(300),
    EMAIL VARCHAR(300) PRIMARY KEY
)
""")
conn.commit()

#header
st.header("Registration Form")
st.subheader("Please fill out the form below")
with st.form(key='student_form'):
    name=st.text_input("Enter your name:",key="name_input")
    password=st.text_input("Enter your password:",type="password",key="password_input")
    email=st.text_input("Enter your email:",key="email_input")
    submit_button=st.form_submit_button(label="Register")
    if submit_button:
        insert_query = "INSERT INTO details(name,password,email) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (name,password,email))
        conn.commit()
        st.success("Form submitted successfully!")
        st.write(f"Name: {name}, password: {password}, Email: {email}")

   
# st.header("Login Form")
# st.subheader("Please enter your credentials to login")
# with st.form(key='login_form'):
#     username=st.text_input("Enter your username:",key="username_input")
#     password=st.text_input("Enter your password:",type="password",key="password_input")
#     login_button=st.form_submit_button(label="Login")



