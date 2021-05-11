#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 10:37:17 2021

@author: trondkjekstad
"""


import pandas as pd
csv_file=pd.read_csv('Pothole_full_data.csv')

def Add_new_column_2_csv(csv_file):
   # print(csv_file)
    csv_file['Ranking']=0.0
    
    csv_file.to_csv('Pothole_full_data.csv',index=False)
    #print(csv_file)
    
    
    
Add_new_column_2_csv(csv_file)






