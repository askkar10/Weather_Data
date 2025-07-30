# download data

# import requests
import requests

r = requests.get("https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt")
readme = r.text
#print(readme)

# get inventory and stations files
r = requests.get("https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-inventory.txt")
inventory_txt = r.text
#print(inventory_txt)

r = requests.get("https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt")
stations_txt = r.text
#print(stations_txt)

# saving both the inventory and stations files
#with open("Weather_Data/inventory.txt", "w") as inventory_file:
#    inventory_file.write(inventory_txt)

#with open("Weather_data/stations.txt", "w",encoding="utf-8") as stations_file:
#    stations_file.write(stations_txt)