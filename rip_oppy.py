#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 13:15:30 2022

@author: user1
"""

##############################################################################
### Imports
##############################################################################

import numpy as np
import subprocess
import requests
import json


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

# Run the query script

script_path = 'test_script.sh'
lat_script = str(lat)
long_script = str(long)
time = 1

list_files = subprocess.run(["bash", script_path, lat_script, long_script])

# read in file and skip 29 rows

data = np.loadtxt('horizons_csv_output.txt', skiprows=30, max_rows=1, dtype=str)
x_pos = float(data[4][:-1])
y_pos = float(data[5][:-1])
z_pos = float(data[6][:-1])


##############################################################################
### Calculation and Execution
##############################################################################

# calculate distance

dist = np.sqrt(x_pos**2 + y_pos**2 + z_pos**2)







##############################################################################
### Command Line Output
##############################################################################

print('Oppy is currently', dist, 'km away from you.')


print('Safe intraplanetary travels from Oppy\'s Alien Family!')

print(r"""\

                        .-.
        .-""`""-.    |(@ @)
     _/`oOoOoOoOo`\_ \ \-/
    '.-=-=-=-=-=-=-.' \/ \
jgs   `-=.=-.-=.=-'    \ /\
         ^  ^  ^       _H_ \


                """)