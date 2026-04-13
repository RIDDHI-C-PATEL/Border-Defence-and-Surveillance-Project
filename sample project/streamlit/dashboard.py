import streamlit as st

st.title("Border Defence Surveillance")

st.sidebar.title("Menu")

option = st.sidebar.selectbox(
"Select",
["Live Detection","Alerts","Prediction"]
)

if option=="Live Detection":
    st.write("Detection Running...")

if option=="Alerts":
    st.write("Showing Alerts")

if option=="Prediction":
    st.write("Prediction Running")