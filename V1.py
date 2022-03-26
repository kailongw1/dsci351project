import streamlit as st
import pandas as pd

st.write("""Group Project, LA safety guideline""")
df = pd.read_csv("adult.csv")
st.print(df)
