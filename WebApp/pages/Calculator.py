from ast import Mult
from email.mime import image
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from multiapp import MultiApp

#title
st.set_page_config(layout="wide")
st.title("Calculator")
st.write("Use this page to calculate your finances. The web app will do the hard work.")


st.image(image, caption= None)
contact = st.sidebar.button("Contact Info")
if contact:
    st.write("Email: jaljon1701@gmail.com")

#Data gather
asset = st.number_input("How much is your assets?")
liability = st.number_input("How much are your liabilities")
if asset and liability:
    st.success("Success!")

