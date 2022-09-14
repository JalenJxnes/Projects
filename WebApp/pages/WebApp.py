#imports
from cmath import e
from msilib.schema import File
from secrets import choice
from tkinter import E
from unicodedata import name
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
import numpy as np
import io
import pandas as pd
from PIL import Image
from st_aggrid import AgGrid
import collections

#title
st.set_page_config(layout="wide")
st.title("Budget Viewer")
st.write("This web app is for you to view and modify a budget and use automation to get a snapshot of what your money situation is.")
st.write("The table below is interactive. Double click any element to change.")
st.sidebar.header("You can use this to navigate the document.")

#sidebar 
with st.sidebar:
    choose = option_menu("Options", ["General info", "Credit Card Info", "Calculator", "Contact"],
                         icons=['house', 'kanban', 'bi-calculator','person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#DDECC3"},
        "icon": {"color": "#6FBBBB", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#e9f3d8"},
        "nav-link-selected": {"background-color": "#bdda8b"},
    }
    )
 
#General Info tab, file uploader
file = st.file_uploader("Upload your Excel file here")
global data
if file is None:
    st.warning("No file uploaded.")
df = pd.read_excel(file)

if file:
    st.success("Success!")
    grid_options = {
    "columnDefs": [
        {
            "headerName": "col1",
            "field": "col1",
            "editable": True,
        },
        {
            "headerName": "col2",
            "field": "col2",
            "editable": False,
        },
    ],
}
    grid_return = AgGrid(df, editable=True)
    new_df = grid_return['data']

