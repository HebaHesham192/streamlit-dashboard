import pandas as pd 
import numpy as np 
import streamlit as st
import plotly.express as px


df=pd.read_csv(r'company_data.csv')
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print(list(df.columns))
cols_to_convert=['target', 'sales', 'bonus']
df[cols_to_convert]=df[cols_to_convert].astype(float)




st.set_page_config(page_title="Car Sales Dashboard", layout="wide")
st.set_page_config(layout="wide")

#-------------------------------------------------------------------------

# sidebar
st.sidebar.markdown('''<h1 style ='text-align:center; margin-top: -65px;'> Car Sales Dashboard </h1>''', unsafe_allow_html=True)
#st.sidebar.header('Car sales dashboard')
from PIL import Image
img=Image.open(r"C:\Users\hesha\Downloads\car.png")
resized_img = img.resize((int(img.width * 0.5), int(img.height * 0.3)))
st.sidebar.image(resized_img)
st.sidebar.write('"An interactive car sales dashboard built with Streamlit and Python, featuring real-time filtering, model comparisons, and visual analytics."')
st.sidebar.markdown (' :star:'' Made by Heba Hesham')
