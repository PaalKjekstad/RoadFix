#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 09:30:33 2021

@author: trondkjekstad
"""

import pandas as pd
from shapely.geometry import Point, LineString , Polygon

cvs_file=pd.read_csv('Pothole_full_data.csv')
length_matrix=pd.read_csv('length_matrix.csv')

def Make_polygon_with_ranked_damages(cvs_file,length_matrix):
    
##----- Finding whitch points to check -----##
    counter=[]
    for i in range(len(cvs_file['Ranking'])):
        if cvs_file['Ranking'][i] != 0 and cvs_file['Ranking'][i]<= 10:
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
            if length_matrix.iloc[counter[0]-1,j+1] <= 20:
                
                #print(length_matrix.iloc[i,j+1],i,j)
                 grouping.append([counter[0]-1,j])
    print(grouping)
     
      
    i=0 ; j=0
    while i in range(len(grouping)-1):
        while j in range(len(grouping)-1):
        
            if grouping[i][0] in grouping[j+1] or grouping[i][1] in grouping[j+1]:
                  List.extend(grouping[i] + grouping[j+1])
                  j=j+1
            else:
                  j=j+1
        i=i+1
        j=i
    
      #---- Remove dublicates ------#
    points_in_close_proximity = []
    for i in List:
          if i not in points_in_close_proximity:
            points_in_close_proximity.append(i)
    print(points_in_close_proximity)
            
            
    print(points_in_close_proximity)
            
            
        
    
    




Make_polygon_with_ranked_damages(cvs_file,length_matrix)
                

                
                
            
    
            
    
    
    