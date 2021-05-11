#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 09:04:39 2021

@author: trondkjekstad
"""

import pandas as pd
file=pd.read_csv('Pothole_full_data.csv')


def Give_out_link_spot_to_pic(cvs_file): # ----- Man writes to machin ------ #
    counter=[]
            
    for i in range(len(cvs_file['Ranking'])):
        if cvs_file['Ranking'][i] == 0:
            counter.append(i)
    return counter #----- Returns a vector with the spots that has not jet been rated -----# 
            

#print(Give_out_link_spot_to_pic(file))