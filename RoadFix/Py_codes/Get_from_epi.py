#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 17:01:07 2021

@author: trondkjekstad
"""

import requests
import json
import pandas as pd



def Get_from_epi():
    response = requests.get('https://five.epicollect.net/api/export/entries/igr?per_page=300')
    raw_data = response.text
    data = json.loads(raw_data)
    data_df = pd.json_normalize(data['data']['entries'])
    #print(data_df)

    
    data_df['lat'] = pd.to_numeric(data_df['1_Where_is_this_poth.latitude'], errors='coerce')
    data_df['long'] =  pd.to_numeric(data_df['1_Where_is_this_poth.longitude'], errors='coerce')
    #print(data_df)
    
    # Adding column
    data_df['Ranking']=0

    return data_df
    

Get_from_epi()




