#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 13:15:30 2022

@author: user1
"""

##############################################################################
### Imports
##############################################################################




##############################################################################
### User Input
##############################################################################

# Welcome the user
#TODO: into with some sort of little poem </3

print('** Welcome to Ode to Oppy!')
print('** Please input your location on Earth.')
print('** lat (-90 to 90 degrees N)')
print('** long (0 to 180 degrees E)')


# Taking input from the user as integer

# Input the latitude, then idiotproof.    
    
lat = float(input("Enter your latitude (deg N): ")) #-90 t0 90

while ((lat < -90) or (lat > 90)):
    print('ERROR: Latitude outside range.')
    print('** Try agiain!')
    lat = float(input("Enter your latitude (deg N): "))

# Input the longitude, then idiotproof.

long = float(input("Enter your longitude (deg E): ")) #0 to 360

while ((long < 0) or (long > 360)):
    print('ERROR: Longitude outside range.')
    print('** Try agiain!')
    long = float(input("Enter your longitude (deg E): "))
 
# Confirm choice

print('** Your coordinates are:', lat, 'deg lat,', long, 'deg long')




##############################################################################
### Query
##############################################################################









##############################################################################
### Calculation and Execution
##############################################################################









##############################################################################
### Command Line Output
##############################################################################