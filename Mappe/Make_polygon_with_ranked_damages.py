#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 09:30:33 2021

@author: trondkjekstad
"""

import pandas as pd
from shapely.geometry import Point, LineString , Polygon

csv_file=pd.read_csv('Pothole_full_data.csv')
length_matrix=pd.read_csv('length_matrix.csv')

def Make_polygon_with_ranked_damages(csv_file,length_matrix):
    
##----- Finding whitch points to check -----##
    counter=[]
    for i in range(len(csv_file['Ranking'])):
        if csv_file['Ranking'][i] != 0 and csv_file['Ranking'][i]<= 10:
            counter.append(i)
   # print(counter)
    ###  If points in counter is in range 20m add to polygon ###
    
    #print(counter,'\n')
    grouping=[]
    List=[]
    i=0
    #print(counter)
    for i in range(len(counter)-1):
        counter.remove(counter[0])
        
        for j in counter:
            #print('j',j)
            if length_matrix.iloc[counter[0]-1,j+1] <= 200:
                
                #print(length_matrix.iloc[i,j+1],i,j)
                 grouping.append([counter[0]-1,j])
    print(grouping, '\n') # All damages within the defined distance in if
     
      
    i=0 ; j=0
   # Big_List=[]
    while i in range(len(grouping)):
        while j in range(len(grouping)-1):
        
            if grouping[i][0] in grouping[j+1] or grouping[i][1] in grouping[j+1]:
                  List.extend(grouping[i] + grouping[j+1])
                  j=j+1
            else:
                #Big_List.append(List)
                j=j+1
        i=i+1
        j=i
    
      #---- Remove dublicates ------#
    #print(List)
    points_in_close_proximity = []
    for i in List:
          if i not in points_in_close_proximity:
            points_in_close_proximity.append(i)
    #print(points_in_close_proximity)
    


    lat=[]
    long=[]
    P=[]
    # ------ If the are more points then 3 points we need to find there coordinates ----- #
    if len(points_in_close_proximity) >= 3:
        for i in points_in_close_proximity:
            lat.append(csv_file.iloc[i,5])
            long.append(csv_file.iloc[i,6])
            P.append(Point(lat[-1],long[-1]))
            
            
            
    unique_P=[]      
    for i in P:
        if i not in unique_P:
            unique_P.append(i)
            
        
    coord_vec=[]
    if len(unique_P) >= 3:
        for i in unique_P:
            coord_vec.append((i.x,i.y))
    return Polygon(coord_vec)
            
            
    
    #print(coord_vec)
    #print(lat,'lat')
    #print(long,'long')
    #print('P',unique_P[0])
    
        
        
            
    
            
            
        
    
    




Make_polygon_with_ranked_damages(csv_file,length_matrix)
                

                
                
            
    
            
    
    
    