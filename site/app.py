import streamlit as st
from supabase import create_client, Client
import pandas as pd
from streamlit_folium import st_folium
import folium

st.set_page_config(layout="wide")

st.title("Solar Panel Deployment Simulator")

# Load secrets
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_ANON_KEY"]

supabase: Client = create_client(url, key)

# Query example table
#response = supabase.table("TEPC_demand").select("*").limit(3).execute()
#df = pd.DataFrame(response.data)
#st.dataframe(df)

df1 = pd.DataFrame({
    'first column': ['Ann Arbor', 'Tucson'],
    })

option = st.selectbox(
    'Select city',
    df1['first column'])

# Map container
map_container = st.container(border=True)
with map_container:
    st.map(data=df1.rename(columns={'first column': 'city'}).assign(lat=[42.2808, 32.2226], lon=[-83.7430, -110.9747]))
    #m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
    #folium.Marker(
    #    [39.949610, -75.150282],
    #    popup="Liberty Bell",
    #    tooltip="Liberty Bell"
    #).add_to(m)

    # call to render Folium map in Streamlit
    #st_data = st_folium(m, width = 725)
    
# City specs container
city_specs = '''
                Number of suitable buildings: {}\n
                Available area for residential buildings: {}sqft\n
                Available area for commercial buildings: {}sqft\n
                Current energy usage: {}kwh\n
                Current energy cost: ${}\n
                Average solar radiation: {}kwh/m2/day
                '''
with st.container(height=300):
    st.markdown(city_specs)

# Power percentage slider
st.slider("Select Power Percentage", 0, 100, 0)
# Commercial coverage slider
st.slider("Select Commercial Coverage", 0, 100, 0)

# Results container
results_container = '''
                    RESULTS\n
                    Total number of buildings required to meet demand: {}\n
                    Residential Buildings: {}\n
                    Commercial Buildings: {}\n

                    Solar Potential\n
                    System size: {}kw\n
                    Annual electricity production: {}kwh\n
                    Roof size suitability: {}sqft\n

                    Financial Benefits:\n
                    System cost: ${}\n
                    First year savings: ${}\n
                    25 year savings: ${}\n
                    Payback period: {} years\n

                    Environmental Benefits:\n
                    Annual CO2 savings: {}lbs CO2e\n
                    Total greenhouse gas reduction over 25 years: {}lbs CO2e\n
                    Equivalent trees planted: {}
                    '''
with st.container(height=300):
    st.markdown(results_container)
