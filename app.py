import streamlit as st
import pandas as pd

st.title("Krishna Wines")
st.header("Welcome to HomePage")
st.subheader("This is a website to showcase different Rum")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")

#with st.container():
#    st.subheader("Old Monk")
#    st.image("artifacts\OldMonk.png")
#    st.subheader("Bacardi")
#    st.image("artifacts\Bacardi-Black.webp")
#    st.subheader("RoyalStag")
#    st.image("artifacts\Royal-Stag.png")

col1, col2, col3 = st.columns([2, 2, 2],gap="medium",vertical_alignment='center',border=True)
col1.subheader("Old Monk")
col1.image("artifacts\OldMonk.png")
col2.subheader("Bacardi")
col2.image("artifacts\Bacardi-Black.webp")
col3.subheader("RoyalStag")
col3.image("artifacts\Royal-Stag.png")  
st.selectbox("Pick one", ["None","Old Monk", "Bacardi","RoyalStag"],placeholder="None")

price = st.slider("Enter Your Budget", min_value=450, max_value=1250,step=250,value=5000)
st.write(f"Your Selected Budget is :- {price}")
st.text_input("Enter Your name")
st.text_input("Enter your COntact no")
st.text_input("Enter your Email Id")
st.text_area("Enter your full address",placeholder="Mumbai")
if st.button("Submit"):
    st.switch_page('pages/form_feedback.py')