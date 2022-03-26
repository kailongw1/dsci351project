import streamlit as st
import pandas as pd

st.write("""Group Project, LA safety guideline""")
df = pd.read_csv("Crime_Data_from_2020_to_Present.csv")
st.print(df)
