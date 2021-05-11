#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 18:39:30 2021

@author: trondkjekstad
"""


import pandas as pd
from shapely.geometry import Point, LineString , Polygon

def Remove_deficient_data(cvs_file):
    
    cvs_file_new=cvs_file.dropna()
    ind=[]
    #print(cvs_file_new.index[0])

    for i in range(len(cvs_file_new.index)):
        ind.append(i)
        cvs_file_new=cvs_file_new.rename(index={cvs_file_new.index[i]:i})
    #print(cvs_file_new.index)
    
    
    ### Not in use ### 
    cvs_file_new['Ranking']=0.0  #------ Makes new column with rating spot ------#
    #print(cvs_file_new)
    cvs_file_new.to_csv('Pothole_full_data.csv')

    

    
Remove_deficient_data(pd.read_csv('form-1_potholes.csv'))