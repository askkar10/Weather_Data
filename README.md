# Weather_Data
Fetch weather data, clean it and then graph it

1) Download weather data, get inventory and stations files, save both on local drive
2) Use dataclass to create a custom inventory class, parse inventory lines and convert some calues to float and int, print some lines to check the data
3) select stations and check for the nearest station to downton chicago
4) select a station and get the station metadata, parse stations and select only one and then print the station
5) fetching the data, fetch daily records for selected station, saving to a text file, read from saved file
6) create func, process all weather data
7) import sqlite3, create weather table, insert weather data into database, select all record from weather where tmax
8) select tmin and tmax
9) import pandas and matplotlib, create data frame, group and print diagram, save the data to excel file (xlsx) and csv file