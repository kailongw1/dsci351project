import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, date, time
import sqlalchemy
import pymysql
import pydeck as pdk
pymysql.install_as_MySQLdb()

my_conn = sqlalchemy.create_engine("mysql+mysqldb://root:<AAaabb?123>@localhost/Crimela")

def main():
    
    menu = ["Home","Rank","Visualization","Filter","About","ContactUs"]
    choice = st.sidebar.selectbox("Menu",menu)
    
    if choice == "Home":
        st.title("Safety LA")
        st.write("""DSCI351 Group Project""")
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
        if option == "01 - Central":
            
            crime = pd.read_sql('select count(*) as "NumOfCrimes in Central" from crime_data_from_2020_to_present where AREA = 01', my_conn)
            st.write('Total Crimes in this Area')
            st.write(crime)
            
            crime = pd.read_sql('select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 01',my_conn)
            st.write('Detailed Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfFelonies" from crime_data_from_2020_to_present where AREA = 01 and `Crm Cd` = 740',my_conn)
            st.write('Total Felonies')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Weapon Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 01 and `Crm Cd` = 740',my_conn)
            st.write('Felonies Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfVehicleRelatedCrimes" from crime_data_from_2020_to_present where AREA = 01 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Total Vehicle Related Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 01 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Vehicle Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfHomicides" from crime_data_from_2020_to_present where AREA = 01 and `Crm Cd` = 110',my_conn)
            st.write('Total Criminal Homicides')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 01 and `Crm Cd` = 110',my_conn)
            st.write('Homicides Info')
            st.write(crime)

          
            crime = pd.read_sql('Select count(*) as "Num of Robbery, Burglary, Stealing Crimes" from crime_data_from_2020_to_present where AREA = 01 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Total Robbery,Burglary,Stealing Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 01 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Crimes Info')
            st.write(crime)

           
            crime = pd.read_sql('Select count(*) as "Num of Rapes" from crime_data_from_2020_to_present where AREA = 01 and `Crm Cd`=  121',my_conn)
            st.write('Total Rapes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 01 and `Crm Cd` = 121',my_conn)
            st.write('Rapes Info')
            st.write(crime)
            
        elif option == "02 - Rampart":
            crime = pd.read_sql('select count(*) as "NumOfCrimes in Central" from crime_data_from_2020_to_present where AREA = 02', my_conn)
            st.write('Total Crimes in this Area')
            st.write(crime)
            
            crime = pd.read_sql('select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 02',my_conn)
            st.write('Detailed Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfFelonies" from crime_data_from_2020_to_present where AREA = 02 and `Crm Cd` = 740',my_conn)
            st.write('Total Felonies')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Weapon Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 02 and `Crm Cd` = 740',my_conn)
            st.write('Felonies Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfVehicleRelatedCrimes" from crime_data_from_2020_to_present where AREA = 02 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Total Vehicle Related Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 02 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Vehicle Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfHomicides" from crime_data_from_2020_to_present where AREA = 02 and `Crm Cd` = 110',my_conn)
            st.write('Total Criminal Homicides')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 02 and `Crm Cd` = 110',my_conn)
            st.write('Homicides Info')
            st.write(crime)

          
            crime = pd.read_sql('Select count(*) as "Num of Robbery, Burglary, Stealing Crimes" from crime_data_from_2020_to_present where AREA = 02 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Total Robbery,Burglary,Stealing Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 02 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Crimes Info')
            st.write(crime)

           
            crime = pd.read_sql('Select count(*) as "Num of Rapes" from crime_data_from_2020_to_present where AREA = 02 and `Crm Cd`=  121',my_conn)
            st.write('Total Rapes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 02 and `Crm Cd` = 121',my_conn)
            st.write('Rapes Info')
            st.write(crime)

        elif option == "03 - Southwest":
            crime = pd.read_sql('select count(*) as "NumOfCrimes in Central" from crime_data_from_2020_to_present where AREA = 03', my_conn)
            st.write('Total Crimes in this Area')
            st.write(crime)
            
            crime = pd.read_sql('select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 03',my_conn)
            st.write('Detailed Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfFelonies" from crime_data_from_2020_to_present where AREA = 03 and `Crm Cd` = 740',my_conn)
            st.write('Total Felonies')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Weapon Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 03 and `Crm Cd` = 740',my_conn)
            st.write('Felonies Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfVehicleRelatedCrimes" from crime_data_from_2020_to_present where AREA = 03 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Total Vehicle Related Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 03 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Vehicle Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfHomicides" from crime_data_from_2020_to_present where AREA = 03 and `Crm Cd` = 110',my_conn)
            st.write('Total Criminal Homicides')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 03 and `Crm Cd` = 110',my_conn)
            st.write('Homicides Info')
            st.write(crime)

          
            crime = pd.read_sql('Select count(*) as "Num of Robbery, Burglary, Stealing Crimes" from crime_data_from_2020_to_present where AREA = 03 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Total Robbery,Burglary,Stealing Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 03 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Crimes Info')
            st.write(crime)

           
            crime = pd.read_sql('Select count(*) as "Num of Rapes" from crime_data_from_2020_to_present where AREA = 03 and `Crm Cd`=  121',my_conn)
            st.write('Total Rapes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 03 and `Crm Cd` = 121',my_conn)
            st.write('Rapes Info')
            st.write(crime)

        elif option == "04 - Hollenbeck":
            crime = pd.read_sql('select count(*) as "NumOfCrimes in Central" from crime_data_from_2020_to_present where AREA = 04', my_conn)
            st.write('Total Crimes in this Area')
            st.write(crime)
            
            crime = pd.read_sql('select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 04',my_conn)
            st.write('Detailed Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfFelonies" from crime_data_from_2020_to_present where AREA = 04 and `Crm Cd` = 740',my_conn)
            st.write('Total Felonies')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Weapon Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 04 and `Crm Cd` = 740',my_conn)
            st.write('Felonies Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfVehicleRelatedCrimes" from crime_data_from_2020_to_present where AREA = 04 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Total Vehicle Related Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 04 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Vehicle Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfHomicides" from crime_data_from_2020_to_present where AREA = 04 and `Crm Cd` = 110',my_conn)
            st.write('Total Criminal Homicides')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 04 and `Crm Cd` = 110',my_conn)
            st.write('Homicides Info')
            st.write(crime)

          
            crime = pd.read_sql('Select count(*) as "Num of Robbery, Burglary, Stealing Crimes" from crime_data_from_2020_to_present where AREA = 04 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Total Robbery,Burglary,Stealing Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 04 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Crimes Info')
            st.write(crime)

           
            crime = pd.read_sql('Select count(*) as "Num of Rapes" from crime_data_from_2020_to_present where AREA = 04 and `Crm Cd`=  121',my_conn)
            st.write('Total Rapes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 04 and `Crm Cd` = 121',my_conn)
            st.write('Rapes Info')
            st.write(crime)

        elif option == "05 - Harbor":
            crime = pd.read_sql('select count(*) as "NumOfCrimes in Central" from crime_data_from_2020_to_present where AREA = 05', my_conn)
            st.write('Total Crimes in this Area')
            st.write(crime)
            
            crime = pd.read_sql('select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 05',my_conn)
            st.write('Detailed Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfFelonies" from crime_data_from_2020_to_present where AREA = 05 and `Crm Cd` = 740',my_conn)
            st.write('Total Felonies')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Weapon Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 05 and `Crm Cd` = 740',my_conn)
            st.write('Felonies Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfVehicleRelatedCrimes" from crime_data_from_2020_to_present where AREA = 05 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Total Vehicle Related Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 05 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Vehicle Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfHomicides" from crime_data_from_2020_to_present where AREA = 05 and `Crm Cd` = 110',my_conn)
            st.write('Total Criminal Homicides')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 05 and `Crm Cd` = 110',my_conn)
            st.write('Homicides Info')
            st.write(crime)

          
            crime = pd.read_sql('Select count(*) as "Num of Robbery, Burglary, Stealing Crimes" from crime_data_from_2020_to_present where AREA = 05 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Total Robbery,Burglary,Stealing Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 05 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Crimes Info')
            st.write(crime)

           
            crime = pd.read_sql('Select count(*) as "Num of Rapes" from crime_data_from_2020_to_present where AREA = 05 and `Crm Cd`=  121',my_conn)
            st.write('Total Rapes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 05 and `Crm Cd` = 121',my_conn)
            st.write('Rapes Info')
            st.write(crime)

        elif option == "06 - Hollywood":
            crime = pd.read_sql('select count(*) as "NumOfCrimes in Central" from crime_data_from_2020_to_present where AREA = 06', my_conn)
            st.write('Total Crimes in this Area')
            st.write(crime)
            
            crime = pd.read_sql('select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 06',my_conn)
            st.write('Detailed Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfFelonies" from crime_data_from_2020_to_present where AREA = 06 and `Crm Cd` = 740',my_conn)
            st.write('Total Felonies')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Weapon Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 06 and `Crm Cd` = 740',my_conn)
            st.write('Felonies Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfVehicleRelatedCrimes" from crime_data_from_2020_to_present where AREA = 06 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Total Vehicle Related Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 06 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Vehicle Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfHomicides" from crime_data_from_2020_to_present where AREA = 06 and `Crm Cd` = 110',my_conn)
            st.write('Total Criminal Homicides')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 06 and `Crm Cd` = 110',my_conn)
            st.write('Homicides Info')
            st.write(crime)

          
            crime = pd.read_sql('Select count(*) as "Num of Robbery, Burglary, Stealing Crimes" from crime_data_from_2020_to_present where AREA = 06 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Total Robbery,Burglary,Stealing Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 06 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Crimes Info')
            st.write(crime)

           
            crime = pd.read_sql('Select count(*) as "Num of Rapes" from crime_data_from_2020_to_present where AREA = 06 and `Crm Cd`=  121',my_conn)
            st.write('Total Rapes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 06 and `Crm Cd` = 121',my_conn)
            st.write('Rapes Info')
            st.write(crime)

        elif option == "07 - Wilshire":
            crime = pd.read_sql('select count(*) as "NumOfCrimes in Central" from crime_data_from_2020_to_present where AREA = 07', my_conn)
            st.write('Total Crimes in this Area')
            st.write(crime)
            
            crime = pd.read_sql('select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 07',my_conn)
            st.write('Detailed Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfFelonies" from crime_data_from_2020_to_present where AREA = 07 and `Crm Cd` = 740',my_conn)
            st.write('Total Felonies')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Weapon Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 07 and `Crm Cd` = 740',my_conn)
            st.write('Felonies Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfVehicleRelatedCrimes" from crime_data_from_2020_to_present where AREA = 07 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Total Vehicle Related Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 07 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Vehicle Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfHomicides" from crime_data_from_2020_to_present where AREA = 07 and `Crm Cd` = 110',my_conn)
            st.write('Total Criminal Homicides')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 07 and `Crm Cd` = 110',my_conn)
            st.write('Homicides Info')
            st.write(crime)

          
            crime = pd.read_sql('Select count(*) as "Num of Robbery, Burglary, Stealing Crimes" from crime_data_from_2020_to_present where AREA = 07 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Total Robbery,Burglary,Stealing Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 07 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Crimes Info')
            st.write(crime)

           
            crime = pd.read_sql('Select count(*) as "Num of Rapes" from crime_data_from_2020_to_present where AREA = 07 and `Crm Cd`=  121',my_conn)
            st.write('Total Rapes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 07 and `Crm Cd` = 121',my_conn)
            st.write('Rapes Info')
            st.write(crime)

        elif option == "08 - West LA":
            crime = pd.read_sql('select count(*) as "NumOfCrimes in Central" from crime_data_from_2020_to_present where AREA = 08', my_conn)
            st.write('Total Crimes in this Area')
            st.write(crime)
            
            crime = pd.read_sql('select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 08',my_conn)
            st.write('Detailed Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfFelonies" from crime_data_from_2020_to_present where AREA = 08 and `Crm Cd` = 740',my_conn)
            st.write('Total Felonies')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Weapon Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 08 and `Crm Cd` = 740',my_conn)
            st.write('Felonies Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfVehicleRelatedCrimes" from crime_data_from_2020_to_present where AREA = 08 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Total Vehicle Related Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 08 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Vehicle Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfHomicides" from crime_data_from_2020_to_present where AREA = 08 and `Crm Cd` = 110',my_conn)
            st.write('Total Criminal Homicides')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 08 and `Crm Cd` = 110',my_conn)
            st.write('Homicides Info')
            st.write(crime)

          
            crime = pd.read_sql('Select count(*) as "Num of Robbery, Burglary, Stealing Crimes" from crime_data_from_2020_to_present where AREA = 08 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Total Robbery,Burglary,Stealing Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 08 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Crimes Info')
            st.write(crime)

           
            crime = pd.read_sql('Select count(*) as "Num of Rapes" from crime_data_from_2020_to_present where AREA = 08 and `Crm Cd`=  121',my_conn)
            st.write('Total Rapes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 08 and `Crm Cd` = 121',my_conn)
            st.write('Rapes Info')
            st.write(crime)

        elif option == "09 - Van Nuys":
            crime = pd.read_sql('select count(*) as "NumOfCrimes in Central" from crime_data_from_2020_to_present where AREA = 09', my_conn)
            st.write('Total Crimes in this Area')
            st.write(crime)
            
            crime = pd.read_sql('select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 09',my_conn)
            st.write('Detailed Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfFelonies" from crime_data_from_2020_to_present where AREA = 09 and `Crm Cd` = 740',my_conn)
            st.write('Total Felonies')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Weapon Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 09 and `Crm Cd` = 740',my_conn)
            st.write('Felonies Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfVehicleRelatedCrimes" from crime_data_from_2020_to_present where AREA = 09 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Total Vehicle Related Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 09 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Vehicle Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfHomicides" from crime_data_from_2020_to_present where AREA = 09 and `Crm Cd` = 110',my_conn)
            st.write('Total Criminal Homicides')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 09 and `Crm Cd` = 110',my_conn)
            st.write('Homicides Info')
            st.write(crime)

          
            crime = pd.read_sql('Select count(*) as "Num of Robbery, Burglary, Stealing Crimes" from crime_data_from_2020_to_present where AREA = 09 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Total Robbery,Burglary,Stealing Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 09 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Crimes Info')
            st.write(crime)

           
            crime = pd.read_sql('Select count(*) as "Num of Rapes" from crime_data_from_2020_to_present where AREA = 09 and `Crm Cd`=  121',my_conn)
            st.write('Total Rapes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 09 and `Crm Cd` = 121',my_conn)
            st.write('Rapes Info')
            st.write(crime)

        elif option == "10 - West Valley":
            crime = pd.read_sql('select count(*) as "NumOfCrimes in Central" from crime_data_from_2020_to_present where AREA = 10', my_conn)
            st.write('Total Crimes in this Area')
            st.write(crime)
            
            crime = pd.read_sql('select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 10',my_conn)
            st.write('Detailed Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfFelonies" from crime_data_from_2020_to_present where AREA = 10 and `Crm Cd` = 740',my_conn)
            st.write('Total Felonies')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Weapon Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 10 and `Crm Cd` = 740',my_conn)
            st.write('Felonies Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfVehicleRelatedCrimes" from crime_data_from_2020_to_present where AREA = 10 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Total Vehicle Related Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 10 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Vehicle Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfHomicides" from crime_data_from_2020_to_present where AREA = 10 and `Crm Cd` = 110',my_conn)
            st.write('Total Criminal Homicides')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 10 and `Crm Cd` = 110',my_conn)
            st.write('Homicides Info')
            st.write(crime)

          
            crime = pd.read_sql('Select count(*) as "Num of Robbery, Burglary, Stealing Crimes" from crime_data_from_2020_to_present where AREA = 10 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Total Robbery,Burglary,Stealing Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 10 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Crimes Info')
            st.write(crime)

           
            crime = pd.read_sql('Select count(*) as "Num of Rapes" from crime_data_from_2020_to_present where AREA = 10 and `Crm Cd`=  121',my_conn)
            st.write('Total Rapes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 10 and `Crm Cd` = 121',my_conn)
            st.write('Rapes Info')
            st.write(crime)

        elif option == "11 - Northeast":
            crime = pd.read_sql('select count(*) as "NumOfCrimes in Central" from crime_data_from_2020_to_present where AREA = 11', my_conn)
            st.write('Total Crimes in this Area')
            st.write(crime)
            
            crime = pd.read_sql('select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 11',my_conn)
            st.write('Detailed Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfFelonies" from crime_data_from_2020_to_present where AREA = 11 and `Crm Cd` = 740',my_conn)
            st.write('Total Felonies')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Weapon Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 11 and `Crm Cd` = 740',my_conn)
            st.write('Felonies Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfVehicleRelatedCrimes" from crime_data_from_2020_to_present where AREA = 11 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Total Vehicle Related Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 11 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Vehicle Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfHomicides" from crime_data_from_2020_to_present where AREA = 11 and `Crm Cd` = 110',my_conn)
            st.write('Total Criminal Homicides')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 11 and `Crm Cd` = 110',my_conn)
            st.write('Homicides Info')
            st.write(crime)

          
            crime = pd.read_sql('Select count(*) as "Num of Robbery, Burglary, Stealing Crimes" from crime_data_from_2020_to_present where AREA = 11 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Total Robbery,Burglary,Stealing Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 11 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Crimes Info')
            st.write(crime)

           
            crime = pd.read_sql('Select count(*) as "Num of Rapes" from crime_data_from_2020_to_present where AREA = 11 and `Crm Cd`=  121',my_conn)
            st.write('Total Rapes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 11 and `Crm Cd` = 121',my_conn)
            st.write('Rapes Info')
            st.write(crime)

        elif option == "12 - 77th Street":
            crime = pd.read_sql('select count(*) as "NumOfCrimes in Central" from crime_data_from_2020_to_present where AREA = 12', my_conn)
            st.write('Total Crimes in this Area')
            st.write(crime)
            
            crime = pd.read_sql('select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 12',my_conn)
            st.write('Detailed Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfFelonies" from crime_data_from_2020_to_present where AREA = 12 and `Crm Cd` = 740',my_conn)
            st.write('Total Felonies')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Weapon Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 12 and `Crm Cd` = 740',my_conn)
            st.write('Felonies Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfVehicleRelatedCrimes" from crime_data_from_2020_to_present where AREA = 12 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Total Vehicle Related Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 12 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Vehicle Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfHomicides" from crime_data_from_2020_to_present where AREA = 12 and `Crm Cd` = 110',my_conn)
            st.write('Total Criminal Homicides')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 12 and `Crm Cd` = 110',my_conn)
            st.write('Homicides Info')
            st.write(crime)

          
            crime = pd.read_sql('Select count(*) as "Num of Robbery, Burglary, Stealing Crimes" from crime_data_from_2020_to_present where AREA = 12 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Total Robbery,Burglary,Stealing Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 12 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Crimes Info')
            st.write(crime)

           
            crime = pd.read_sql('Select count(*) as "Num of Rapes" from crime_data_from_2020_to_present where AREA = 12 and `Crm Cd`=  121',my_conn)
            st.write('Total Rapes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 12 and `Crm Cd` = 121',my_conn)
            st.write('Rapes Info')
            st.write(crime)

        elif option == "13 - Newton":
            crime = pd.read_sql('select count(*) as "NumOfCrimes in Central" from crime_data_from_2020_to_present where AREA = 13', my_conn)
            st.write('Total Crimes in this Area')
            st.write(crime)
            
            crime = pd.read_sql('select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 13',my_conn)
            st.write('Detailed Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfFelonies" from crime_data_from_2020_to_present where AREA = 13 and `Crm Cd` = 740',my_conn)
            st.write('Total Felonies')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Weapon Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 13 and `Crm Cd` = 740',my_conn)
            st.write('Felonies Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfVehicleRelatedCrimes" from crime_data_from_2020_to_present where AREA = 13 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Total Vehicle Related Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 13 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Vehicle Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfHomicides" from crime_data_from_2020_to_present where AREA = 13 and `Crm Cd` = 110',my_conn)
            st.write('Total Criminal Homicides')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 13 and `Crm Cd` = 110',my_conn)
            st.write('Homicides Info')
            st.write(crime)

          
            crime = pd.read_sql('Select count(*) as "Num of Robbery, Burglary, Stealing Crimes" from crime_data_from_2020_to_present where AREA = 13 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Total Robbery,Burglary,Stealing Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 13 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Crimes Info')
            st.write(crime)

           
            crime = pd.read_sql('Select count(*) as "Num of Rapes" from crime_data_from_2020_to_present where AREA = 13 and `Crm Cd`=  121',my_conn)
            st.write('Total Rapes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 13 and `Crm Cd` = 121',my_conn)
            st.write('Rapes Info')
            st.write(crime)

        elif option == "14 - Pacific":
            crime = pd.read_sql('select count(*) as "NumOfCrimes in Central" from crime_data_from_2020_to_present where AREA = 14', my_conn)
            st.write('Total Crimes in this Area')
            st.write(crime)
            
            crime = pd.read_sql('select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 14',my_conn)
            st.write('Detailed Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfFelonies" from crime_data_from_2020_to_present where AREA = 14 and `Crm Cd` = 740',my_conn)
            st.write('Total Felonies')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Weapon Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 14 and `Crm Cd` = 740',my_conn)
            st.write('Felonies Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfVehicleRelatedCrimes" from crime_data_from_2020_to_present where AREA = 14 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Total Vehicle Related Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 14 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Vehicle Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfHomicides" from crime_data_from_2020_to_present where AREA = 14 and `Crm Cd` = 110',my_conn)
            st.write('Total Criminal Homicides')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 14 and `Crm Cd` = 110',my_conn)
            st.write('Homicides Info')
            st.write(crime)

          
            crime = pd.read_sql('Select count(*) as "Num of Robbery, Burglary, Stealing Crimes" from crime_data_from_2020_to_present where AREA = 14 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Total Robbery,Burglary,Stealing Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 14 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Crimes Info')
            st.write(crime)

           
            crime = pd.read_sql('Select count(*) as "Num of Rapes" from crime_data_from_2020_to_present where AREA = 14 and `Crm Cd`=  121',my_conn)
            st.write('Total Rapes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 14 and `Crm Cd` = 121',my_conn)
            st.write('Rapes Info')
            st.write(crime)

        elif option == "15 - N Hollywood":
            crime = pd.read_sql('select count(*) as "NumOfCrimes in Central" from crime_data_from_2020_to_present where AREA = 15', my_conn)
            st.write('Total Crimes in this Area')
            st.write(crime)
            
            crime = pd.read_sql('select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 15',my_conn)
            st.write('Detailed Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfFelonies" from crime_data_from_2020_to_present where AREA = 15 and `Crm Cd` = 740',my_conn)
            st.write('Total Felonies')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Weapon Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 15 and `Crm Cd` = 740',my_conn)
            st.write('Felonies Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfVehicleRelatedCrimes" from crime_data_from_2020_to_present where AREA = 15 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Total Vehicle Related Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 15 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Vehicle Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfHomicides" from crime_data_from_2020_to_present where AREA = 15 and `Crm Cd` = 110',my_conn)
            st.write('Total Criminal Homicides')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 15 and `Crm Cd` = 110',my_conn)
            st.write('Homicides Info')
            st.write(crime)

          
            crime = pd.read_sql('Select count(*) as "Num of Robbery, Burglary, Stealing Crimes" from crime_data_from_2020_to_present where AREA = 15 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Total Robbery,Burglary,Stealing Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 15 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Crimes Info')
            st.write(crime)

           
            crime = pd.read_sql('Select count(*) as "Num of Rapes" from crime_data_from_2020_to_present where AREA = 15 and `Crm Cd`=  121',my_conn)
            st.write('Total Rapes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 15 and `Crm Cd` = 121',my_conn)
            st.write('Rapes Info')
            st.write(crime)

        elif option == "16 - Foothill":
            crime = pd.read_sql('select count(*) as "NumOfCrimes in Central" from crime_data_from_2020_to_present where AREA = 16', my_conn)
            st.write('Total Crimes in this Area')
            st.write(crime)
            
            crime = pd.read_sql('select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 16',my_conn)
            st.write('Detailed Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfFelonies" from crime_data_from_2020_to_present where AREA = 16 and `Crm Cd` = 740',my_conn)
            st.write('Total Felonies')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Weapon Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 16 and `Crm Cd` = 740',my_conn)
            st.write('Felonies Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfVehicleRelatedCrimes" from crime_data_from_2020_to_present where AREA = 16 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Total Vehicle Related Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 16 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Vehicle Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfHomicides" from crime_data_from_2020_to_present where AREA = 16 and `Crm Cd` = 110',my_conn)
            st.write('Total Criminal Homicides')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 16 and `Crm Cd` = 110',my_conn)
            st.write('Homicides Info')
            st.write(crime)

          
            crime = pd.read_sql('Select count(*) as "Num of Robbery, Burglary, Stealing Crimes" from crime_data_from_2020_to_present where AREA = 16 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Total Robbery,Burglary,Stealing Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 16 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Crimes Info')
            st.write(crime)

           
            crime = pd.read_sql('Select count(*) as "Num of Rapes" from crime_data_from_2020_to_present where AREA = 16 and `Crm Cd`=  121',my_conn)
            st.write('Total Rapes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 16 and `Crm Cd` = 121',my_conn)
            st.write('Rapes Info')
            st.write(crime)

        elif option == "17 - Devonshire":
            crime = pd.read_sql('select count(*) as "NumOfCrimes in Central" from crime_data_from_2020_to_present where AREA = 17', my_conn)
            st.write('Total Crimes in this Area')
            st.write(crime)
            
            crime = pd.read_sql('select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 17',my_conn)
            st.write('Detailed Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfFelonies" from crime_data_from_2020_to_present where AREA = 17 and `Crm Cd` = 740',my_conn)
            st.write('Total Felonies')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Weapon Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 17 and `Crm Cd` = 740',my_conn)
            st.write('Felonies Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfVehicleRelatedCrimes" from crime_data_from_2020_to_present where AREA = 17 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Total Vehicle Related Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 17 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Vehicle Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfHomicides" from crime_data_from_2020_to_present where AREA = 17 and `Crm Cd` = 110',my_conn)
            st.write('Total Criminal Homicides')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 17 and `Crm Cd` = 110',my_conn)
            st.write('Homicides Info')
            st.write(crime)

          
            crime = pd.read_sql('Select count(*) as "Num of Robbery, Burglary, Stealing Crimes" from crime_data_from_2020_to_present where AREA = 17 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Total Robbery,Burglary,Stealing Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 17 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Crimes Info')
            st.write(crime)

           
            crime = pd.read_sql('Select count(*) as "Num of Rapes" from crime_data_from_2020_to_present where AREA = 17 and `Crm Cd`=  121',my_conn)
            st.write('Total Rapes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 17 and `Crm Cd` = 121',my_conn)
            st.write('Rapes Info')
            st.write(crime)

        elif option == "18 - Southeast":
            crime = pd.read_sql('select count(*) as "NumOfCrimes in Central" from crime_data_from_2020_to_present where AREA = 18', my_conn)
            st.write('Total Crimes in this Area')
            st.write(crime)
            
            crime = pd.read_sql('select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 18',my_conn)
            st.write('Detailed Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfFelonies" from crime_data_from_2020_to_present where AREA = 18 and `Crm Cd` = 740',my_conn)
            st.write('Total Felonies')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Weapon Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 18 and `Crm Cd` = 740',my_conn)
            st.write('Felonies Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfVehicleRelatedCrimes" from crime_data_from_2020_to_present where AREA = 18 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Total Vehicle Related Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 18 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Vehicle Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfHomicides" from crime_data_from_2020_to_present where AREA = 18 and `Crm Cd` = 110',my_conn)
            st.write('Total Criminal Homicides')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 18 and `Crm Cd` = 110',my_conn)
            st.write('Homicides Info')
            st.write(crime)

          
            crime = pd.read_sql('Select count(*) as "Num of Robbery, Burglary, Stealing Crimes" from crime_data_from_2020_to_present where AREA = 18 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Total Robbery,Burglary,Stealing Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 18 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Crimes Info')
            st.write(crime)

           
            crime = pd.read_sql('Select count(*) as "Num of Rapes" from crime_data_from_2020_to_present where AREA = 18 and `Crm Cd`=  121',my_conn)
            st.write('Total Rapes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 18 and `Crm Cd` = 121',my_conn)
            st.write('Rapes Info')
            st.write(crime)

        elif option == "19 - Mission":
            crime = pd.read_sql('select count(*) as "NumOfCrimes in Central" from crime_data_from_2020_to_present where AREA = 19', my_conn)
            st.write('Total Crimes in this Area')
            st.write(crime)
            
            crime = pd.read_sql('select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 19',my_conn)
            st.write('Detailed Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfFelonies" from crime_data_from_2020_to_present where AREA = 19 and `Crm Cd` = 740',my_conn)
            st.write('Total Felonies')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Weapon Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 19 and `Crm Cd` = 740',my_conn)
            st.write('Felonies Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfVehicleRelatedCrimes" from crime_data_from_2020_to_present where AREA = 19 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Total Vehicle Related Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 19 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Vehicle Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfHomicides" from crime_data_from_2020_to_present where AREA = 19 and `Crm Cd` = 110',my_conn)
            st.write('Total Criminal Homicides')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 19 and `Crm Cd` = 110',my_conn)
            st.write('Homicides Info')
            st.write(crime)

          
            crime = pd.read_sql('Select count(*) as "Num of Robbery, Burglary, Stealing Crimes" from crime_data_from_2020_to_present where AREA = 19 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Total Robbery,Burglary,Stealing Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 19 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Crimes Info')
            st.write(crime)

           
            crime = pd.read_sql('Select count(*) as "Num of Rapes" from crime_data_from_2020_to_present where AREA = 19 and `Crm Cd`=  121',my_conn)
            st.write('Total Rapes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 19 and `Crm Cd` = 121',my_conn)
            st.write('Rapes Info')
            st.write(crime)

        elif option == "20 - Olympic":
            crime = pd.read_sql('select count(*) as "NumOfCrimes in Central" from crime_data_from_2020_to_present where AREA = 20', my_conn)
            st.write('Total Crimes in this Area')
            st.write(crime)
            
            crime = pd.read_sql('select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 20',my_conn)
            st.write('Detailed Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfFelonies" from crime_data_from_2020_to_present where AREA = 20 and `Crm Cd` = 740',my_conn)
            st.write('Total Felonies')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Weapon Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 20 and `Crm Cd` = 740',my_conn)
            st.write('Felonies Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfVehicleRelatedCrimes" from crime_data_from_2020_to_present where AREA = 20 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Total Vehicle Related Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 20 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Vehicle Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfHomicides" from crime_data_from_2020_to_present where AREA = 20 and `Crm Cd` = 110',my_conn)
            st.write('Total Criminal Homicides')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 20 and `Crm Cd` = 110',my_conn)
            st.write('Homicides Info')
            st.write(crime)

          
            crime = pd.read_sql('Select count(*) as "Num of Robbery, Burglary, Stealing Crimes" from crime_data_from_2020_to_present where AREA = 20 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Total Robbery,Burglary,Stealing Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 20 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Crimes Info')
            st.write(crime)

           
            crime = pd.read_sql('Select count(*) as "Num of Rapes" from crime_data_from_2020_to_present where AREA = 20 and `Crm Cd`=  121',my_conn)
            st.write('Total Rapes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 20 and `Crm Cd` = 121',my_conn)
            st.write('Rapes Info')
            st.write(crime)
        
        else:
            crime = pd.read_sql('select count(*) as "NumOfCrimes in Central" from crime_data_from_2020_to_present where AREA = 21', my_conn)
            st.write('Total Crimes in this Area')
            st.write(crime)
            
            crime = pd.read_sql('select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 21',my_conn)
            st.write('Detailed Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfFelonies" from crime_data_from_2020_to_present where AREA = 21 and `Crm Cd` = 740',my_conn)
            st.write('Total Felonies')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Weapon Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 21 and `Crm Cd` = 740',my_conn)
            st.write('Felonies Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfVehicleRelatedCrimes" from crime_data_from_2020_to_present where AREA = 21 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Total Vehicle Related Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 21 and `Crm Cd` = 330 or `Crm Cd` = 510',my_conn)
            st.write('Vehicle Crimes Info')
            st.write(crime)

            
            crime = pd.read_sql('Select count(*) as "NumOfHomicides" from crime_data_from_2020_to_present where AREA = 21 and `Crm Cd` = 110',my_conn)
            st.write('Total Criminal Homicides')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 21 and `Crm Cd` = 110',my_conn)
            st.write('Homicides Info')
            st.write(crime)

          
            crime = pd.read_sql('Select count(*) as "Num of Robbery, Burglary, Stealing Crimes" from crime_data_from_2020_to_present where AREA = 21 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Total Robbery,Burglary,Stealing Crimes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Crm Cd Desc`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 21 and `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480',my_conn)
            st.write('Crimes Info')
            st.write(crime)

           
            crime = pd.read_sql('Select count(*) as "Num of Rapes" from crime_data_from_2020_to_present where AREA = 21 and `Crm Cd`=  121',my_conn)
            st.write('Total Rapes')
            st.write(crime)
            crime = pd.read_sql('Select `TIME OCC`,`Vict Age`,`Vict Sex`,LOCATION from Crimela.crime_data_from_2020_to_present where AREA = 21 and `Crm Cd` = 121',my_conn)
            st.write('Rapes Info')
            st.write(crime)
        
    elif choice == "Rank":
        st.subheader("Safety Index Ranking")
        col1,col2,col3 = st.columns(3)
        rank  = pd.read_sql('select `AREA NAME`,count(*) FROM Crimela.crime_data_from_2020_to_present group by `AREA NAME` order by count(*)',my_conn)
        col1.write('Rank according to total crimes')
        col1.write(rank)
        rank = pd.read_sql('select `AREA NAME`,count(*) FROM Crimela.crime_data_from_2020_to_present where `Crm Cd` = 110 or `Crm Cd` = 740  group by `AREA NAME` order by count(*)',my_conn)
        col2.write('Rank (Felony+Homicide)')
        col2.write(rank)
        rank = pd.read_sql('select `AREA NAME`,count(*) FROM Crimela.crime_data_from_2020_to_present where `Crm Cd` = 121  group by `AREA NAME` order by count(*)',my_conn)
        col3.write('Rank (Rape)')
        col3.write(rank)

        col4,col5 = st.columns(2)
        rank = pd.read_sql('select `AREA NAME`,count(*) FROM Crimela.crime_data_from_2020_to_present where `Crm Cd` = 210 or `Crm Cd` = 310 or `Crm Cd` = 442 or `Crm Cd` = 354 or `Crm Cd` = 420 or `Crm Cd` = 341 or `Crm Cd` = 440 or `Crm Cd` = 352 or `Crm Cd` = 480 group by `AREA NAME` order by count(*)',my_conn)
        col4.write('Rank (Robbery+Burglary+Stealing)')
        col4.write(rank)
        rank = pd.read_sql('select `AREA NAME`,count(*) FROM Crimela.crime_data_from_2020_to_present where `Crm Cd` = 330 or `Crm Cd` = 510 group by `AREA NAME` order by count(*)', my_conn)
        col5.write('Rank (Vehicle Related Crimes)')
        col5.write(rank)

        #westla 228000
        #77th 175000
        #harbor 171000
        #Hollenback 200000
        #Hollywood 300000
        #Central 40000
        #mission 225849
        #Rampart 164961
        #Devonshire 219136
        #Newton 267342
        #N Hollywood 220000
        #Northeast 250000
        #Southeast 150000
        #Southwest 165000
        #Foothill 182214
        #Olympic 230000
        #Topanga 220000
        #Van Nuys 325000
        #West  Valley 196840
        #wilshire 251000
        #pacific 200000

        st.write('Rank according to Crime/Population Ratio')
        numCrimes  = pd.read_sql('select count(*) as "01 Ratio" FROM Crimela.crime_data_from_2020_to_present where AREA = 01',my_conn)
        ratio01 = numCrimes/40000
        st.write('Central: ',ratio01)
        numCrimes  = pd.read_sql('select count(*) as "02 Ratio" FROM Crimela.crime_data_from_2020_to_present where AREA = 02',my_conn)
        ratio02 = numCrimes/164961
        st.write('Rampart: ',ratio02)
        numCrimes  = pd.read_sql('select count(*) as "03 Ratio" FROM Crimela.crime_data_from_2020_to_present where AREA = 03',my_conn)
        ratio03 = numCrimes/165000
        st.write('Southwest: ',ratio03)
        numCrimes  = pd.read_sql('select count(*) as "04 Ratio" FROM Crimela.crime_data_from_2020_to_present where AREA = 04',my_conn)
        ratio04 = numCrimes/200000
        st.write('Hollenbeck: ',ratio04)
        numCrimes  = pd.read_sql('select count(*) as "05 Ratio" FROM Crimela.crime_data_from_2020_to_present where AREA = 05',my_conn)
        ratio05 = numCrimes/171000
        st.write('Harbor: ',ratio05)
        numCrimes  = pd.read_sql('select count(*) as "06 Ratio" FROM Crimela.crime_data_from_2020_to_present where AREA = 06',my_conn)
        ratio06 = numCrimes/300000
        st.write('Hollywood: ',ratio06)
        numCrimes  = pd.read_sql('select count(*) as "07 Ratio" FROM Crimela.crime_data_from_2020_to_present where AREA = 07',my_conn)
        ratio07 = numCrimes/251000
        st.write('Wilshire: ',ratio07)
        numCrimes  = pd.read_sql('select count(*) as "08 Ratio" FROM Crimela.crime_data_from_2020_to_present where AREA = 08',my_conn)
        ratio08 = numCrimes/228000
        st.write('West LA: ',ratio08)
        numCrimes  = pd.read_sql('select count(*) as "09 Ratio" FROM Crimela.crime_data_from_2020_to_present where AREA = 09',my_conn)
        ratio09 = numCrimes/325000
        st.write('Van Nuys: ',ratio09)
        numCrimes  = pd.read_sql('select count(*) as "10 Ratio" FROM Crimela.crime_data_from_2020_to_present where AREA = 10',my_conn)
        ratio10 = numCrimes/196840
        st.write('West Valley: ',ratio10)
        numCrimes  = pd.read_sql('select count(*) as "11 Ratio" FROM Crimela.crime_data_from_2020_to_present where AREA = 11',my_conn)
        ratio11 = numCrimes/250000
        st.write('Northeast: ',ratio11)
        numCrimes  = pd.read_sql('select count(*) as "12 Ratio" FROM Crimela.crime_data_from_2020_to_present where AREA = 12',my_conn)
        ratio12 = numCrimes/175000
        st.write('77th Street: ',ratio12)
        numCrimes  = pd.read_sql('select count(*) as "13 Ratio" FROM Crimela.crime_data_from_2020_to_present where AREA = 13',my_conn)
        ratio13 = numCrimes/267342
        st.write('Newton: ',ratio13)
        numCrimes  = pd.read_sql('select count(*) as "14 Ratio" FROM Crimela.crime_data_from_2020_to_present where AREA = 14',my_conn)
        ratio14 = numCrimes/200000
        st.write('Pacific: ',ratio14)
        numCrimes  = pd.read_sql('select count(*) as "15 Ratio" FROM Crimela.crime_data_from_2020_to_present where AREA = 15',my_conn)
        ratio15 = numCrimes/220000
        st.write('N Hollywood: ',ratio15)
        numCrimes  = pd.read_sql('select count(*) as "16 Ratio" FROM Crimela.crime_data_from_2020_to_present where AREA = 16',my_conn)
        ratio16 = numCrimes/182214
        st.write('Foothill: ',ratio16)
        numCrimes  = pd.read_sql('select count(*) as "17 Ratio" FROM Crimela.crime_data_from_2020_to_present where AREA = 17',my_conn)
        ratio17 = numCrimes/219136
        st.write('Devonshire: ',ratio17)
        numCrimes  = pd.read_sql('select count(*) as "18 Ratio" FROM Crimela.crime_data_from_2020_to_present where AREA = 18',my_conn)
        ratio18 = numCrimes/150000
        st.write('Southeast: ',ratio18)
        numCrimes  = pd.read_sql('select count(*) as "19 Ratio" FROM Crimela.crime_data_from_2020_to_present where AREA = 19',my_conn)
        ratio19 = numCrimes/225849
        st.write('Mission: ',ratio19)
        numCrimes  = pd.read_sql('select count(*) as "20 Ratio" FROM Crimela.crime_data_from_2020_to_present where AREA = 20',my_conn)
        ratio20 = numCrimes/230000
        st.write('Olympic: ',ratio20)
        numCrimes  = pd.read_sql('select count(*) as "21 Ratio" FROM Crimela.crime_data_from_2020_to_present where AREA = 21',my_conn)
        ratio21 = numCrimes/220000
        st.write('Topanga: ',ratio21)

        list = [ratio01,ratio02,ratio03,ratio04,ratio05,ratio06,ratio07,ratio08,ratio09,ratio10,ratio11,ratio12,ratio13,ratio14,ratio15,ratio16,ratio17,ratio18,ratio19,ratio20,ratio21]
        
        st.write(list)
        
        

    #Cath updated
    elif choice == "Visualization":
        st.title("Visualization")
        st.subheader("""Area Ranking in Map""")
        data = pd.read_csv("Crime_Data_from_2020_to_Present.csv")

        #display data and rename
        df = pd.DataFrame(data)
        df.dropna()
        df.rename(
        columns=({ 'LAT': 'lat', 'LON': 'lon'}), 
        inplace=True,)

        area = st.sidebar.multiselect(
        "Select the Area:",
        options=df["AREA NAME"].unique(),
        default=df["AREA NAME"].unique().all()
        )
        df = df[df['AREA NAME'].isin(area)]
        df["DATE OCC"] = pd.to_datetime(df["DATE OCC"])
        

        df = df[
        (df["DATE OCC"] >= pd.to_datetime('2022-01-01'))]
        df = df[['lon','lat']]
        st.write(f"Data Points: {len(df)}")
        df.dropna()
        st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
         latitude=df['lat'].mean(),
         longitude=df['lon'].mean(),
         zoom=11,
         pitch=50,
     ),
        layers=[
        pdk.Layer(
            'HexagonLayer',
            data=df,
            get_position='[lon, lat]',
            radius=100,
            elevation_scale=7,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
         ),
         pdk.Layer(
             'ScatterplotLayer',
             data=df,
             get_position='[lon, lat]',
             get_color='[200, 30, 0, 160]',
             get_radius=100,
         ),
        ],
     )
                
    )    

    elif choice == "Filter":
        st.title(":chart_with_upwards_trend: Crime Filter")

        # ---- READ CSV ----
        df = pd.read_csv("Crime_Data_from_2020_to_Present.csv")


        st.sidebar.header("Please Filter Here:")
        area = st.sidebar.multiselect(
        "Select the Area:",
        options=df["AREA NAME"].unique(),
        default=[]
        )

        crime_type = st.sidebar.multiselect(
        "Select the Crime Type:",
        options=df["Crm Cd Desc"].unique(),
        default=[],
        )

        vict_sex = st.sidebar.multiselect(
            "Select the Victim Sex:",
            options=df["Vict Sex"].unique(),
            default=[]
        )
        
        location = st.sidebar.multiselect(
        "Select the Location:",
        options=df["Premis Desc"].unique(),
        default=[]
        )
        
        # timeline
        df["LAT"]=pd.to_numeric(df["LAT"])
        df["LON"]=pd.to_numeric(df["LON"])
        df = pd.DataFrame(df)
        df["DATE OCC"] = pd.to_datetime(df["DATE OCC"])
        min_occurence = pd.to_datetime(min(df["DATE OCC"])).date()
        max_occurence = pd.to_datetime(max(df["DATE OCC"])).date()
        start_time,end_time = st.sidebar.slider("Timeline", min_value=min_occurence, max_value=max_occurence,value=[min_occurence,max_occurence])
        
        start_age,end_age = st.sidebar.slider("Victim Age Range:", min_value=0, max_value=100, step=1, value=[0,100])
    

        df = df[df['AREA NAME'].isin(area)]
        df = df[df['Crm Cd Desc'].isin(crime_type)]
        df = df[df['Vict Sex'].isin(vict_sex)]
        df = df[df['Premis Desc'].isin(location)]
        df = df[(df["DATE OCC"] >= pd.to_datetime(start_time)) & (df["DATE OCC"] <= pd.to_datetime(end_time))]
        df = df[(df["Vict Age"] >= pd.to_numeric(start_age)) & (df["Vict Age"] <= pd.to_numeric(end_age))]

        
        st.markdown("##")
        
        
        # Total Crime
        total_crime = int(df["DATE OCC"].count())
        danger_level = round(df["DATE OCC"].count()/10, 1)
        skull = ":skull:" * int(round(danger_level, 0))

        
        
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Total Selected Crime:")
            st.subheader(f"{total_crime:,} Crime(s)")
        with right_column:
            st.subheader("Selected Danger Level:")
            st.subheader(f"{danger_level} {skull}")

            
        st.markdown("""---""")
        
        st.write("Detailed data presented here:")
        
        st.dataframe(df)
        
            

    elif choice == "About":
        st.title("Safety LA")
        st.write("""DSCI351 Group Project""")
        st.subheader("About")
        st.write("""Every year, there are around 50 million visitors entering LA, a place where gun violence and crime rampaged across (the city experienced 1,459 victims shot and 397 murders last year). While the situation is even worse since the onset of the pandemic, new travelers who entered the region are unfamiliar with the security level and unaware of the danger level in different LA regions. For this project, we aim to help visitors to avoid hazards and secure their safety by providing an app, which includes functions like providing safety guide and map, ranking of safety level in a certain area, alerting for high-risk areas, etc. Our project is also designed to change locals’ stereotypes. Neighborhoods could possibly be associated with unsafe impressions because of film and television works. On the other hand, We provide lively updated  data that demonstrate the safety levels from a more subjective perspective. 
""")

    else:
        st.title("Safety LA")
        st.write("""DSCI351 Group Project""")
        st.subheader("ContactUs")
        st.write("""Kailong Wang: kailongw@usc.edu""")
        st.write("""Xiayu Li: xiayuli@usc.edu""")
        st.write("""Catherine Lin: linzhiyi@usc.edu""")
        


if __name__ ==  '__main__':
    main()


