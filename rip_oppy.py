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
import time
import sys

##############################################################################
### Useful Functions
##############################################################################

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)


##############################################################################
### User Input
##############################################################################

# Welcome the user

delay_print('** Welcome to Ode to Oppy!')
time.sleep(1)
print()
delay_print('** Please input your location on Earth.')
time.sleep(0.5)
print()
print('** lat (-90 to 90 degrees N)')
print('** long (0 to 180 degrees E)')


# Taking input from the user as integer

# Input the latitude, then idiotproof.    
    
lat = float(input("Enter your latitude (deg N): ")) #-90 t0 90

while ((lat < -90) or (lat > 90)):
    print('ERROR: Latitude outside range.')
    print('** Try again!')
    lat = float(input("Enter your latitude (deg N): "))

# Input the longitude, then idiotproof.

long = float(input("Enter your longitude (deg E): ")) #0 to 360

while ((long < 0) or (long > 360)):
    print('ERROR: Longitude outside range.')
    print('** Try again!')
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
current_time = 1

list_files = subprocess.run(["bash", script_path, lat_script, long_script])

# read in file and skip 29 rows

results_path = 'results2.txt'

data = np.loadtxt(results_path, skiprows=36, max_rows=1, dtype=str)
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

#%%

print()

print('** Oppy is currently', dist, 'km away from you.')
time.sleep(0.75)

print()
time.sleep(0.75)
print()

pause_poem = 0.9
delay_print('It seems to me you lived your life')
print()
time.sleep(pause_poem)
delay_print('like a rover in the wind')
print()
time.sleep(pause_poem)
delay_print('never fading with the sunset')
print()
time.sleep(pause_poem)
delay_print('when the dust set in.')
print()
time.sleep(pause_poem)
delay_print('Your tracks will always fall here,')
print()
time.sleep(pause_poem)
delay_print('among Mars\' reddest hills;')
print()
time.sleep(pause_poem)
delay_print('your candle\'s burned out long before')
print()
time.sleep(pause_poem)
delay_print('your science ever will.')
print()
time.sleep(1.5)

print()

delay_print('** Safe intraplanetary travels from Oppy\'s Alien Family!')
print()

print(r"""\

                        .-.
        .-""`""-.    |(@ @)
     _/`oOoOoOoOo`\_ \ \-/
    '.-=-=-=-=-=-=-.' \/ \
jgs   `-=.=-.-=.=-'    \ /\
         ^  ^  ^       _H_ \


                """)
                
                
                
                
time.sleep(5)
print()
print()
print()
print()
print()
print()

print('Poem from @MarsCuriosity')
print('ASCII art from the Ascii Art Archive')
print('Positional data from')
print(r"""     
     ___    _____     ___                                                      
    /_ /|  /____/ \  /_ /|       Horizons On-line Ephemeris System v4.92       
    | | | |  __ \ /| | | |       Solar System Dynamics Group                   
 ___| | | | |__) |/  | | |__     Jet Propulsion Laboratory                     
/___| | | |  ___/    | |/__ /|   Pasadena, CA, USA                             
|_____|/  |_|/       |_____|/                                                  
 

      """)