from PIL import Image
from streamlit_option_menu import option_menu
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
import re
from streamlit.components.v1 import html
mydb= mysql.connector.connect(
   host="localhost",
   user="root",
   password="0129",
   database="sahi_yog"
)
mycursor=mydb.cursor()
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

st.set_page_config(page_title="Sahiयोग",page_icon=":moneybag:" , layout="wide")

with st.container():
   selected=option_menu(
      menu_title=None,
      options=["Home","Signup","Login"],
      icons=["house","box-arrow-in-right","box-arrow-in-right"],
      default_index=0,
      orientation="horizontal",
      styles={
      "nav-link":{
      "--hover-color":"#5A5A5A"
      }
      }
   )


def form():
   st.title("Finance Details")
   # DataFrame
   df = pd.read_csv(r'C:\Users\sudha\Downloads\sahyog 3.csv')

   # form to take input from the user
   loan_amnt = st.text_input("Enter loan amount:")
   interest = ['Select'] + [15, 20, 25]
   selected_interest = st.selectbox("Select interest rate of loan (Rates may vary in a range)", interest, index=0)
   year = st.slider("Experience in current business", 1, 45)
   turnover = st.text_input("Enter your yearly turnover: ")
   family_inc = st.text_input("Enter your net income: ")
   


   # submit button
   submitted = st.button("Submit")

   if not loan_amnt or not turnover or not family_inc or selected_interest == 'Select':
      st.warning("Please fill in all the fields.")
   else:
      # convert input strings to appropriate data types
      loan_amnt = float(loan_amnt)
      selected_interest = int(selected_interest)
      turnover = float(turnover)
      family_inc = float(family_inc)
      year = int(year)
      
      
      
      # filter the dataframe
      results_df = df[(df[' Maximum Loan Amount'] >= loan_amnt) & 
                     (df["min.Interest rate"] <= selected_interest) &
                     (df['minimum Business turnover'] <= turnover) &
                     (df['Minimal Annual Income'] <= family_inc) &
                     (df['minimum years in current business']<= year)]
      
      
      # Display search results to the user
      if results_df.empty:
         st.write("No matches found.")
      else:
         num_results = len(results_df)
         st.write(f"{num_results} result{'s' if num_results>1 else ''} found.")
         st.write(results_df)

         # Create a bar graph with bank names and interest rates
         plt.bar(results_df['Bank Name'], results_df['min.Interest rate'])
         plt.xlabel('Bank Name', fontsize=7)
         plt.ylabel('Interest Rate',fontsize=7)
         plt.title('Interest Rates of Eligible Banks',fontsize=7)
         plt.xticks(fontsize=7)
         st.pyplot()

def set_style():
    """
    Function to apply custom CSS styles
    """
    style = f"""
    /* Add your custom CSS styles here */
    .stTextInput,.stSelectbox,.stSlider  {{
        background-color: #242254;
        border: 1px solid #28a781;
        border-radius: 5px;
        padding: 8px; /* Adjust padding */
        margin-bottom: 10px;
        font-size: 16px;
        color: #FFFF;
    }}
    """

    # Apply the custom CSS
    st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)

# Call the set_style function at the beginning of your Streamlit app
set_style()

def home_page():
   st.markdown(
   f"""
   <style>
   {open("design.css").read()} 
   </style>
   """,
   unsafe_allow_html=True,
   )

   # Style the content with lilac color
   lilac_text = """
   Welcome to our website, your one-stop destination for small business loans. We understand that getting the right financing is crucial for the success of any small business, and that's why we have created a platform that enables you to compare all the available loans in the market and find the best option that fits your unique needs and eligibility criteria. Our website is designed specifically for small business owners who are looking to grow their business, expand their operations, or fund a new project. We provide a comprehensive list of all the loans available in the market, including traditional bank loans, merchant cash advances, and more. Our comparison tool allows you to filter loans based on your specific eligibility criteria, such as credit score, business revenue, and time in business. We provide all the necessary information you need to make an informed decision, including interest rates, loan amounts, repayment terms, and other relevant details. With our user-friendly interface and streamlined process, you can easily compare loans and find the best option for your business in just a few clicks. So whether you're just starting out or have an established business, our website is the perfect place to find the financing you need to take your business to the next level. Explore our loan comparison tool today and discover the perfect loan for your small business.
   """

   # Container with white background
   st.markdown(
      "<div class='white-container'>"
      "<h1 class='centered-title'>Welcome to Sahiyog</h1>"
      f"<p class='lilac-text'>{lilac_text}</p>"
      "</div>",
      unsafe_allow_html=True,
   )
   st.markdown(
      "<div class='skyblue-container'>"
      "<h1 style='text-align:center; font-size:5em;color:white;'>About Sahiyog</h1>"
      "<p style= 'font-size:30px;'>Sahiyog is your one-stop destination for all your support needs, We provide a wide range of services to help you in your daily life."
      "Our website is designed specifically for small business owners who are looking to: </p>"
      "<ul>"
      "<li style= 'font-size:2em;'>Grow their business</li>"
      "<li style= 'font-size:2em;'>Expand their operations</li>"
      "<li style= 'font-size:2em;'>Fund their projects</li>"
      "</ul>"
      "</div>",
      unsafe_allow_html=True,
   )


   st.markdown(
      "<div class='yellow-container'>"
      "<h1 style='text-align:center; font-size:5em;color:#4CAF50;'>About Our Team</h1>"
      "<p style= 'font-size:30px;'>Sahiyog is a team of dedicated individuals who are here to assist you with various services.We provide all the necessary information you need to make an informed decision, including: </p>"
      "<ul>"
      "<li style= 'font-size:2em;'>Internet rates</li>"
      "<li style= 'font-size:2em;'>Loan amounts</li>"
      "<li style= 'font-size:2em;'>Repayment term</li>"
      "<li style= 'font-size:2em;'>And other relevant details</li>"
      "</ul>"
      "</div>",
      unsafe_allow_html=True,
   )

   st.markdown(
      "<div class='pink-container'>"
      "<h1 style='text-align:center; font-size:5em;color:white;'>Our Services</h1>"
      "<p style= 'font-size:30px;'>We offer a variety of services, Our comparison tool allows you to filter loans based on your specific eligibility criteria, such as: </p>"
      "<ul>"
      "<li style= 'font-size:2em;'>Credit Profile</li>"
      "<li style= 'font-size:2em;'>Business revenue</li>"
      "<li style= 'font-size:2em;'>Time in business</li>"
      "</ul>"
      "</div>",
      unsafe_allow_html=True,
   )


   st.markdown(
      "<div class='orange-container'>"
      "<h1 style='text-align:center; font-size:5em;color:#4CAF50;'>Contact Us</h1>"
      "<p style= 'font-size:30px;'>You can reach us at:</p>"
      "<ul>"
      "<li style= 'font-size:30px;'>Email: contact@sahiyog.com</li>"
      "<li style= 'font-size:30px;'>Phone: +1-123-456-7890</li>"
      "</ul>"
      "</div>",
      unsafe_allow_html=True,
   )

def signup_page():
   st.header("Create new account")
   col1,col2,col3=st.columns(3)
   with col1:
      fl = st.text_input('First Name')
   with col2:
      ml = st.text_input('Middle Name')
   with col3:
      ll = st.text_input('Last Name')
   col4,col5=st.columns(2)
   with col4:
      contact = st.text_input('Contact Number')
   with col5:
      mail = st.text_input('Email')
   col6,col7=st.columns(2)
   with col6:
      age = st.slider('Age', 18, 64,format="%d")
   with col7:
      gender = st.selectbox('Gender', ('Select','Male', 'Female'))
   col8,col9=st.columns(2)
   with col8:
      b_name=st.text_input("Your business name")
   with col9:
      sector=st.selectbox('Business Category',('Select','Public','Private'))
   password=st.text_input("Create password",type='password')

   if st.button("Signup"):
      # Validate contact number
    contact_regex = r"^\d{10}$"  # Assumes a 10-digit phone number
    if not re.match(contact_regex, contact):
        st.error("Please enter a valid 10-digit phone number")


    # Validate email
    email_regex = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
    if not re.match(email_regex, mail):
        st.error("Please enter a valid email address")
    sql="insert into user_table(First_Name,Middle_Name,Last_Name,Contact_Number,email,age,gender,Business_name,Sector,password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(fl,ml,ll,contact,mail,age,gender,b_name,sector,password)
    mycursor.execute(sql,val)
    mydb.commit()
    st.success("Succesfully created an account.")
    st.info("Go to Login page to login")

def login_page():
   st.subheader('Login to your account')
   col1,col2=st.columns(2)
   with col1:
      number = st.text_input('Contact Number')
   with col2:
      password = st.text_input('Password', type='password')

   # Create a button to submit the form
   if st.button('Login'):
        # Check if the name, password, and mobile number match the data in the database
        mycursor.execute("SELECT * FROM user_table WHERE Contact_Number=%s AND password=%s ", (number, password))
        user = mycursor.fetchone()
        if user:
            st.session_state.logged_in = True
            st.success('Login successful')
        else:
            st.error('Invalid name, password')

if selected=="Home":
   home_page()
elif selected=="Signup":
   signup_page()
elif selected=="Login":
   login_page()  
if st.session_state.logged_in:
   form()

mydb.close()
