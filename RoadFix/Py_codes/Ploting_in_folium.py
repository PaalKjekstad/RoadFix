#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 19:24:03 2021

@author: trondkjekstad
"""


#import packages
import webbrowser
import geopandas as gpd
import folium
import matplotlib.pyplot as plt

import Get_from_epi as Gfe
csv_file_old=Gfe.Get_from_epi()

import Remove_deficient_data as Rdd
csv_file_1=Rdd.Remove_deficient_data(csv_file_old)

import Write_rating as Wr
csv_file=Wr.Write_rating(csv_file_1)

import Make_points as Mp
Point_list=Mp.Make_points(csv_file)

#print(csv_file)

#print(csv_file['lat'])

def Ploting_in_folium(csv_file):
    plot_data_3=csv_file.loc[(csv_file['Ranking']<=10)&(csv_file['Ranking']>=8)]
    plot_data_2=csv_file.loc[(csv_file['Ranking']<=7)&(csv_file['Ranking']>=4)]
    plot_data=csv_file.loc[csv_file['Ranking']<=3]
    

    
    m = folium.Map(location=[53.5500,-2.4333], zoom_start=6, tiles='CartoDB positron')
    for indice, row in plot_data.iterrows():
        folium.Marker(
            location=[row["lat"], row["long"]],
            icon=folium.map.Icon(color='green')
            ).add_to(m)
        
    for indice, row in plot_data_2.iterrows():
        folium.Marker(
            location=[row["lat"], row["long"]],
            icon=folium.map.Icon(color='orange')
            ).add_to(m)
        
    for indice, row in plot_data_3.iterrows():
        folium.Marker(
            location=[row["lat"], row["long"]],
            icon=folium.map.Icon(color='red')
            ).add_to(m)
        
    m.save('/Users/trondkjekstad/Desktop/RoadFix_1.1/RoadFix-main-3/RoadFix/templates/map.html')  
        
        
        
        # Alt fra M er tatt fra https://stackoverflow.com/questions/62204655/cant-plot-the-map-with-folium
        
Ploting_in_folium(csv_file)