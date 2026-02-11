# app.py
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

df = pd.read_csv("blue_ribbon.csv")

st.title("레스토랑 지도")

ribbon_filter = st.slider("리본 개수", 0, 3, 0)

filtered = df[df["ribbon_num"] >= ribbon_filter]

m = folium.Map(location=[37.5, 127], zoom_start=7)

for _, row in filtered.iterrows():
    folium.CircleMarker(
        location=[row["lat"], row["lng"]],
        popup=row["nameKR"]
    ).add_to(m)

st_folium(m)



