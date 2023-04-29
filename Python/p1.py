from PIL import Image
from streamlit_option_menu import option_menu
import streamlit as st
import pandas as pd
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


st.set_page_config(page_title="Sahiयोग",page_icon=":moneybag:" , layout="wide")
img_contact_form=Image.open("images/Sahi.png")
st.image(img_contact_form)


with st.container():
   selected=option_menu(
      menu_title=None,
      options=["Home","Signup","Login","Finance Details"],
      icons=["house","box-arrow-in-right","box-arrow-in-right","info-circle-fill"],
      default_index=0,
      orientation="horizontal",
      styles={
      "nav-link":{
      "--hover-color":"#5A5A5A"
      }
      }
   )
def form():
   # DataFrame
   df = pd.read_csv(r'C:\Users\sudha\Downloads\sahyog 2.csv')

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


if selected=="Home":
   
   st.header("Introduction")
   # st.info("Welcome to our website, your one-stop destination for small business loans. We understand that getting the right financing is crucial for the success of any small business, and that's why we have created a platform that enables you to compare all the available loans in the market and find the best option that fits your unique needs and eligibility criteria.Our website is designed specifically for small business owners who are looking to grow their business, expand their operations, or fund a new project. \n We provide a comprehensive list of all the loans available in the market, including traditional bank loans , merchant cash advances, and more.Our comparison tool allows you to filter loans based on your specific eligibility criteria, such as credit score, business revenue, and time in business. We provide all the necessary information you need to make an informed decision, including interest rates, loan amounts, repayment terms, and other relevant details.With our user-friendly interface and streamlined process, you can easily compare loans and find the best option for your business in just a few clicks. So whether you're just starting out or have an established business, our website is the perfect place to find the financing you need to take your business to the next level.Explore our loan comparison tool today and discover the perfect loan for your small business.")
   st.info("Welcome to our website, your one-stop destination for small business loans. "
         "We understand that getting the right financing is crucial for the success of any small business, "
         "and that's why we have created a platform that enables you to compare all the available loans in the market "
         "and find the best option that fits your unique needs and eligibility criteria.")

   st.info("Our website is designed specifically for small business owners who are looking to: ")
   
   st.info("- Grow their business")
   
   st.info("- Expand their operations")
   
   st.info("- Fund a new project")

   st.info("We provide a comprehensive list of all the loans available in the market, including: ")
   
   st.info("- Traditional bank loans")
   
   st.info("- Merchant cash advances")
   
   st.info("- And more")

   st.info("Our comparison tool allows you to filter loans based on your specific eligibility criteria, such as: ")
   
   st.info("- Credit score")
   st.info("- Business revenue")
   st.info("- Time in business")

   st.info("We provide all the necessary information you need to make an informed decision, including: ")
   
   st.info("- Interest rates")
   st.info("- Loan amounts")
   st.info("- Repayment terms")
   st.info("- And other relevant details")

   st.write("With our user-friendly interface and streamlined process, you can easily compare loans and find the best option "
            "for your business in just a few clicks. So whether you're just starting out or have an established business, "
            "our website is the perfect place to find the financing you need to take your business to the next level.")

   st.write("Explore our loan comparison tool today and discover the perfect loan for your small business.")
   
   

if selected=="Signup":
   st.header("Create new account")
   fl = st.text_input('First Name')
   ml = st.text_input('Middle Name')
   ll = st.text_input('Last Name')
   contact = st.text_input('Contact Number')
   mail = st.text_input('Email')
   age = st.slider('Age', 18, 64)
   gender = st.selectbox('Gender', ('Select','Male', 'Female'))
   b_name=st.text_input("Your business name")
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


if selected=="Login":
   st.subheader('Login to your account')
   number = st.text_input('Contact Number')
   password = st.text_input('Password', type='password')
    
    # Create a button to submit the form
   if st.button('Login'):
        # Check if the name, password, and mobile number match the data in the database
        mycursor.execute("SELECT * FROM user_table WHERE Contact_Number=%s AND password=%s ", (number, password))
        user = mycursor.fetchone()
        if user:
            st.success('Login successful') 
        else:
            st.error('Invalid name, password')

if selected=="About":
   st.header("About")

if selected=="Finance Details":
   form()

mydb.close()
