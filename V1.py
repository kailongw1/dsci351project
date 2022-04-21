import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, date, time
#import sqlalchemy
#import pymysql
#pymysql.install_as_MySQLdb()

#my_conn = sqlalchemy.create_engine("mysql+mysqldb://root:<AAaabb?123>@localhost/Crimela")
#crime = pd.read_sql('select count(*) from crime_data_from_2020_to_present', my_conn)
#crime

def main():
    st.title("Safety LA")
    st.write("""DSCI351 Group Project""")
    menu = ["Home","About","ContactUs"]
    choice = st.sidebar.selectbox("Menu",menu)
    
    if choice == "Home":
        st.subheader("Home Page")
        data = pd.read_csv("Crime_Data_from_2020_to_Present.csv")

        #display data and rename
        df = pd.DataFrame(data)
        df.rename(
        columns=({ 'LAT': 'lat', 'LON': 'lon'}), 
        inplace=True,)

        
        
        st.dataframe(df)

        #map function starts
        df["lat"]=pd.to_numeric(df["lat"]) 
        df["lon"]=pd.to_numeric(df["lon"])
        df = pd.DataFrame(data)

        
        df["DATE OCC"] = pd.to_datetime(df["DATE OCC"])
        
        min_occurence = pd.to_datetime(min(df["DATE OCC"])).date()
        max_occurence = pd.to_datetime(max(df["DATE OCC"])).date()

       
        start_time,end_time = st.slider("Timeline", min_value=min_occurence, max_value=max_occurence,value=[min_occurence,max_occurence])


        st.write(f"Filtering between {start_time} & {end_time}")
        df = df[
        (df["DATE OCC"] >= pd.to_datetime(start_time)) & (df["DATE OCC"] <= pd.to_datetime(end_time))]
        st.write(f"Data Points: {len(df)}")
        

    
        st.map(df,8)
        #map function ends
        
        option = st.selectbox(
         'Which area you want to know about?',
         ('01 - Central', '02 - Rampart', '03 - Southwest','04 - Hollenbeck','05 - Harbor','06 - Hollywood','07 - Wilshire','08 - West LA','09 - Van Nuys','10 - West Valley','11 - Northeast','12 - 77th Street','13 - Newton','14 - Pacific','15 - N Hollywood','16 - Foothill','17 - Devonshire','18 - Southeast','19 - Mission','20 - Olympic','21 - Topanga'))

        st.write('You selected:', option)


    elif choice == "About":
        st.subheader("About")
        st.write("""Every year, there are around 50 million visitors entering LA, a place where gun violence and crime rampaged across (the city experienced 1,459 victims shot and 397 murders last year). While the situation is even worse since the onset of the pandemic, new travelers who entered the region are unfamiliar with the security level and unaware of the danger level in different LA regions. For this project, we aim to help visitors to avoid hazards and secure their safety by providing an app, which includes functions like providing safety guide and map, ranking of safety level in a certain area, alerting for high-risk areas, etc. Our project is also designed to change locals’ stereotypes. Neighborhoods could possibly be associated with unsafe impressions because of film and television works. On the other hand, We provide lively updated  data that demonstrate the safety levels from a more subjective perspective. 
""")

    else:
        st.subheader("ContactUs")
        st.write("""Kailong Wang: kailongw@usc.edu""")
        st.write("""Xiayu Li: xiayuli@usc.edu""")
        st.write("""Zhiying(Catherine) Lin: linzhiyi@usc.edu""")
        


if __name__ ==  '__main__':
    main()
