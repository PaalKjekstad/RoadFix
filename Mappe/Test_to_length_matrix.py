#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 17:52:31 2021

@author: trondkjekstad
"""

import pandas as pd
from shapely.geometry import Point, LineString , Polygon
cvs_file=pd.read_csv('length_matrix.csv')
#print(cvs_file)
nr_of_mistakes=0
for i in range(len(cvs_file.iloc[:,1])): # siden databasen sin titel starter med , iloc[0,0]=P1
    dist=cvs_file.iloc[i,i+1]
    for j in range(len(cvs_file.iloc[1,:])-1):
        if cvs_file.iloc[j,i+1] - cvs_file.iloc[i,j+1] != 0:
            print("Wrong data in one of the points ",i,' og ',j)
            nr_of_mistakes=nr_of_mistakes+1
            
            
    if dist != 0:
        print("Feil ved punkt ",i)
        nr_of_mistakes=nr_of_mistakes+1
        #print(dist)
        
if nr_of_mistakes==0:
    print('\nThe data set is complete, no error')

#print(cvs_file.iloc[189,0])
#print(cvs_file.iloc[0,1]-cvs_file.iloc[1,1])
        
            
    #for j in range(len(cvs_file.iloc[:,1])):
        
        