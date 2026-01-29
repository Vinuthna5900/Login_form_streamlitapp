import streamlit as st
#header
st.header("Student Information Form(Vinuthna Reddy)")
st.markdown("---------")
#Title
st.title("Enter Your Details")
st.markdown("---------")
#SubHeader
st.subheader("Please fill out the form below")

#Markdown
st.markdown("---------")

#Text
st.text("This form collects basic information about students.")
st.markdown("---------")

#Write in includes text, numbers, data etc.
st.write("Hello Streamlit!")
st.write(42)
st.write(3.14)
st.write({"name": "Alice", "age": 23})  
st.write([1, 2, 3, 4, 5])
st.markdown("---------")

#caption
st.caption("vinun")
st.markdown("---------")

#markdown:display formated text
st.markdown("**Bold Text**")
st.markdown("*Italic Text*")        
st.markdown("~~Strikethrough Text~~")
st.markdown("> Blockquote Text")
st.markdown("`Inline Code`")
st.markdown("<h3 style='color:Red;'>Colored Header</h3>", unsafe_allow_html=True)
st.markdown("---------")


#st.code():Code method to display code snippets with syntax highlighting
st.code("""
def greet(name):
    return f"Hello, {name}!"
print(greet("World"))
""", language='python')
st.markdown("---------")

#Latex: display mathematical 
# expressions
st.latex(r'''E = mc^2''')
st.markdown("---------")
#Divider:method to separate content sections
st.divider()
#Button:to create a button
if st.button("Submit"):
    st.write("Form Submitted!")
    st.success("Form loaded successfully!")
    st.balloons()
else:
    st.write("Button not clicked yet.")
    st.error("Please fill out the form.")
st.markdown("---------")

#TextInput:to create a text input field
name = st.text_input("Enter your name:",key="name_input")
st.write(f"Hello, {name}!")
st.markdown("---------")


#if user put wrong input
names= st.text_input("Enter your name:",key="names_input2")
if names == "":
    st.warning("Name cannot be empty. Please enter your name.")
elif not names.isalpha():
    st.error("Invalid Input. Name should only contain letters.")
else:
    st.success(f"Hello, {names}!")
st.markdown("---------")

#TextArea:to create a larger text input field
text_area = st.text_area("Enter your address:",key="address_input")
st.write(f"Your address is: {text_area}")
st.divider()

#Radio Button:to create radio buttons for selection
st_radio= st.radio("Select your gender  :", ("Male", "Female", "Other"))
st.write(f"You selected: {st_radio}")

#Select Box:to create a dropdown selection box
st_selectbox= st.selectbox("Select your country  :", ("USA", "Canada", "UK", "Australia"))
st.write(f"You selected: {st_selectbox}")

#Multiselect:to create a multiselect box
st_multiselect= st.multiselect("Select your favorite subjects  :", ("Math", "Science", "History", "Art"))
st.write(f"You selected: {st_multiselect}")

#Slider:to create a slider for numerical input
st_slider= st.slider("Select your age  :", 0, 5, 1)
st.write(f"You selected: {st_slider}")

#file_uploader:to upload files
uploaded_file = st.file_uploader("Upload your profile picture:", type=["jpg", "png", "jpeg"])
st.write("You uploaded:", uploaded_file)
st.divider()

#form method to create a form
with st.form("student_form"):
    student_name = st.text_input("Name:", key="form_name")
    student_age = st.number_input("Age:", key="form_age")
    student_email = st.text_input("Email:", key="form_email")
    submit= st.form_submit_button("Submit Form")

if submit:
    st.write(student_name, student_age, student_email)

#form to create submit button with green colour button

with st.form("login"):
    username = st.text_input("Username:", key="login_username")
    password = st.text_input("Password:", type="password", key="login_password")
    login_submit= st.form_submit_button("Login", help="Click to login", type="primary")
if login_submit:
    st.success("login successful!")
st.divider()
#coloumns:to create multiple columns for layout
col1, col2, col3 = st.columns(3)
with col1:
    st.header("Column 1")
    st.write(" these is Column 1")
with col2:
    st.header("Column 2")
    st.write(" these is Column 2")
with col3:
    st.header("Column 3")
    st.write(" these is Column 3")

st.divider()
#container:to group related content together
con= st.container()
with con:
    st.header("Container Section")
    st.write("This content is inside a container.")
st.divider()
#table  method to display data in tabular format

data={
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [23, 30, 25],
    "City": ["New York", "Los Angeles", "Chicago"]
 }
st.table(data)

#sidebar:to create a sidebar for navigation or additional options
st.sidebar.title("Sidebar Menu")
option = st.sidebar.radio("Select an option:", ["Home", "Profile", "Settings"])

st.sidebar.write(f"You selected: {option}")
