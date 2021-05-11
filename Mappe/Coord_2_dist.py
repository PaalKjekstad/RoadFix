#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 16:46:54 2021

@author: trondkjekstad
"""

from shapely.geometry import Point
from math import sqrt

def Coord_2_dist(P1,P2):
    
    # P1=(long1,lat1)  -- & -- P2=(long2,lat2)
    # Long x-direct ->   Lat z-direct 
    R=6371000 #Radius of earth in [m]
    
    d_ang_x=float(P1.x)-float(P2.x)
    d_ang_y=P1.y-P2.y
    
    d_x=d_ang_x*R
    d_y=d_ang_y*R
    
    dist_between=sqrt(d_x**2 + d_y**2)
    return dist_between





#P=Point([51.426041,-2.522599])
#print(Coord_2_dist(P,P))