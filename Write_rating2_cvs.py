#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 08:56:34 2021

@author: trondkjekstad
"""



import pandas as pd
cvs_file=pd.read_csv('Pothole_full_data.csv')

import Give_out_link_spot_to_pic as golstp
counter=golstp.Give_out_link_spot_to_pic(cvs_file)

def Write_rating_2_cvs(cvs_file,counter,ranking): # ----- Man writes to machin ------ #
#---- Counter from Give_out_link_spot_to_pic.py and ranking from html code ----#
    cvs_file['Ranking'][counter[0]]=ranking
    counter.remove(counter[0])
    
    cvs_file.to_csv('Pothole_full_data.csv',index=False)
    
               
    
Write_rating_2_cvs(cvs_file,counter,10)
