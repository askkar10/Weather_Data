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

# parsing the inventory data
# use dataclass to create a custom inventory class

from dataclasses import dataclass
@dataclass
class Inventory:
    station: str
    latitude: float
    longitude: float
    element: str
    start: int
    end: int

# parse inventory lines and convert some values to floats and ints
inventory = [Inventory(x[0:11], float(x[12:20]), float(x[21:30]), x[31:35],
                       int(x[36:40]), int(x[41:45])) for x in inventory_txt.split("\n")
                       if x.startswith("US")]

for line in inventory[:10]:
    print(line)