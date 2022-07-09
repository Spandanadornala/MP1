import streamlit as st
import joblib
model = joblib.load('MOBILE-PRICE')
st.title("MOBILE & IT'S PRICES")
ip = st.text_input('Enter the mobile name')
op = model.predict([ip])
if st.button('Go'):
  st.title(op[0])
