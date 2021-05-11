#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 09:45:19 2021

@author: trondkjekstad
"""

import pandas as pd
from shapely.geometry import Point, LineString , Polygon
cvs_file=pd.read_csv('Pothole_full_data.csv')
#print(cvs_file)

import Make_points_of_damages as Mpod
List_P=Mpod.Make_points_of_damages(cvs_file)
# Makes list of shaply Points of all points in CSV 

import Coord_2_dist as c_2_d  # Imports code that finds distance between to points with coords
# Takes in to points in form of Shaply Points




def Find_distance_to_matrix(List_of_Points):

    name_vek=[]
    for i in range(len(List_of_Points)):
        name_vek.append('P '+str(i))  
    #print(name_vek)
    
    
    matrise=pd.DataFrame('0',columns=name_vek,index=name_vek)
    #print(matrise)
    matrise.to_csv('length_matrix.csv')
    
    for i in range(len(List_of_Points)): # Vertikal
        for j in range(len(List_of_Points)):# Horisontal 
            dist=c_2_d.Coord_2_dist(List_of_Points[i],List_of_Points[j])
            #print(dist)
            matrise.iloc[j,i]=dist
            #length_between_points.append(List_of_Points[i].distance(List_of_Points[j]))
            #p=i+j
        #matrise=pd.DataFrame(length_between_points,column='P '+str(j),index='P '+str(i))
     
    matrise.to_csv('length_matrix.csv')
    #print(List_of_Points[0])
    
    
            
Find_distance_to_matrix(List_P)            
            
            