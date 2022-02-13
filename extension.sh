#!/bin/sh
#imports horizon
telnet ssd.jpl.nasa.gov 6775
#inputs opportunity target
g: -354.656219,-2.328078,0 @ 499
#Set ephemeris
E
#Sets vectors option
v
#Sets coordinates option
coord
#Sets reference planes
eclip
#Sets Starting time
2004-Jan-29 00:00
#Sets End time
2004-Feb-28 00:00
#Sets frequency of observation
1d
#Confirms settings(yes)
y
#Gets new line
N
