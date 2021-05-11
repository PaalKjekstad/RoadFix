#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 09:23:41 2021

@author: trondkjekstad
"""
import pandas as pd
from shapely.geometry import Point, LineString , Polygon

def Make_points_of_damages(cvs_file):
    lat=cvs_file['lat_1_Where_is_this_poth']
    long=cvs_file['long_1_Where_is_this_poth']
    #print(lat)
    #print(long)
    
    ## Making a list of shaply points ##
    list_of_points=[]
    for i in range(len(lat)):
        
        list_of_points.append(Point(lat[i],long[i]))

    #print(list(list_of_points[1].coords))
    #print(list(list_of_points[1].coords)[0][0])
    #print(list_of_points)
    P_1=(list_of_points[0].coords)[0]
    P_2=(list_of_points[3].coords)[0]
    #print('P1',P_1,'P2',P_2)
    #point_dis=list_of_points[0].distance(list_of_points[1])
    #print(point_dis)
    return list_of_points
    
    


#print(Make_points_of_damages('form-1_potholes.csv'))



cvs_file=pd.read_csv("Pothole_full_data.csv")
#print(cvs_file)
#print(cvs_file[0:1])

#LIST=Make_points_of_damages(cvs_file)
#print(LIST[1])
#print(LIST[1].x)

## categoris ##
#ec5_uuid 1
#created_at 2
#uploaded_at 3
#title 4
#lat_1_Where_is_this_poth 5
#long_1_Where_is_this_poth 6
#accuracy_1_Where_is_this_poth 7
#UTM_Northing_1_Where_is_this_poth 8
#UTM_Easting_1_Where_is_this_poth 9
#UTM_Zone_1_Where_is_this_poth 10
#2_Please_take_a_phot 11
#3_Tutorial_GroupSmal 12