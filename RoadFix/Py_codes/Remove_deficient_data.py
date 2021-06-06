#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 18:39:30 2021

@author: trondkjekstad
"""

import pandas as pd
import Get_from_epi as Gfe
cvs_file=Gfe.Get_from_epi()


def Remove_deficient_data(cvs_file):
    
    cvs_file_new=cvs_file.dropna()
    ind=[]
    #print(cvs_file_new.index[1])

    for i in range(len(cvs_file_new.index)):
        ind.append(i)
        cvs_file_new=cvs_file_new.rename(index={cvs_file_new.index[i]:i})
        
        
    #print(cvs_file_new.index)
    #print(cvs_file_new['long'][160:185])
    
    return cvs_file_new

#print(Remove_deficient_data(cvs_file))