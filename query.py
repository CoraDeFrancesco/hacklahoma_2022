# -*- coding: utf-8 -*-
import os

# This takes in the pre-made text file with the batch commands for Horizons and 
# queries Horizons by using the separate Python file horizons.py
def query_horizons():
    os.system("python horizons.py horizons_params.txt > results.txt")
    
# This makes a text file that is used as input to Horizons, containing all necessary parameters for a query
def make_input_file(earth_lat,earth_long,start_time,stop_time):
    opp_mars_long = -354.656219
    opp_mars_lat = -2.328078
    txtstring = "!$$SOF\nCOMMAND='g: " + str(opp_mars_long) + ", " + str(opp_mars_lat) + ", 0 @ 499'\nOBJ_DATA='NO'\nMAKE_EPHEM='YES'\nEPHEM_TYPE='V'\nCENTER='coord'\nREF_PLANE='ECLIPTIC'\nCOORD_TYPE='GEODETIC'\nSITE_COORD='" + str(earth_lat) + "," + str(earth_long) + ",0'\nSTART_TIME='" + start_time + "'\nSTOP_TIME='" + stop_time + "'\nSTEP_SIZE='1 day'\nREF_SYSTEM='ICRF'\nOUT_UNITS='KM-S'\nVEC_TABLE='3'\nVEC_CORR='NONE'\nCSV_FORMAT='YES'"
    with open('horizons_params.txt', 'w') as f:
        f.write(txtstring)

make_input_file(-97.4395,35.2226,'2022-FEB-12 19:10','2022-FEB-13 19:10')
query_horizons()
    