# rip-oppy
# #Project Description
rip-oppy is a retro-theme interface that outputs a precise distance between the user's coordinates and the rover Opportunity's (Oppy) location on Mars at the current time. This project was created as a tribute for Opportunity's legacy of Mars exploration and data collection. 
Some of the technologies used to develop this project and its purposes include:
-  The JPL Horizons solar system data and ephemeris computation service from NASA (https://ssd.jpl.nasa.gov/horizons/) to create a query to get coordinates for both the user and Opportunity's location with respect to the same reference frame. 
- A reverse geocode function (credit to https://github.com/richardpenman/reverse_geocode) to convert addresses to accurate geocoordinates
- A function that computes the user's current time in UTC  <br />

In the future, some of the features that can be implemented in the program are Oppy's birthday, statistics about the mission, and even calculating the dates when Oppy will be the closest to the user's location on Earth.
# # How to Install and Run rip-oppy
Install rip-oppy by typing in your command line `pip install rip-oppy ` 
# #How to Use the Project 
Input your terrestrial coordinates for latitude and longitude in the given format or choose one of the given cities. The program accepts northern latitudes in decimal degrees from 0 to 90, southern latitudes from 0 to -90, eastern longitudes from 0 to 180, and western longitudes from 0 to -180.
# # Credits
**Team:** <br />
- Cora de Francesco: https://github.com/CoraDeFrancesco  <br />
- Alex Parsells: https://github.com/parsellsx   <br />
- Cosme Aquino Ovelar   <br />



