#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 18:02:06 2021

@author: trondkjekstad
"""

from sqlalchemy import create_engine
import pandas as pd
import geopandas as gpd

import Get_from_epi as Gfe
csv_file=Gfe.Get_from_epi()

import Make_points as Mlop
Point_file=Mlop.Make_points(csv_file)


##------- Adds both "point csv" and "pothole csv" -------##

def Add_2_postgresql(PotHole_file,Point_file):
    # Total information on potholes
    engine = create_engine('postgresql://postgres:19Pjok96@localhost:5432/Paal_SE4GI') 
    csv_file.to_sql('potholes', engine, if_exists = 'replace', index=False)
    csv_file_sql = pd.read_sql_table('potholes',engine)
    
    # Information of the Points r
    engine = create_engine('postgresql://postgres:19Pjok96@localhost:5432/Paal_SE4GI') 
    csv_file.to_sql('Points', engine, if_exists = 'replace', index=False)
    csv_file_sql = pd.read_sql_table('Points',engine)
    
    
Add_2_postgresql(csv_file,Point_file)



