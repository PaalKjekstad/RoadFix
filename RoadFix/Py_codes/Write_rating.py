#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 22:39:35 2021

@author: trondkjekstad
"""

from random import randint

import Get_from_epi as Gfe

import Remove_deficient_data as Rdd
csv_file=Rdd.Remove_deficient_data(Gfe.Get_from_epi())





def Write_rating(file):
        
    for i in range(len(csv_file)):
       # print(i)
        file.iloc[i,14]=randint(1,10)
        
    return file
    
    

#print(Write_rating(csv_file))