import json
import folium
with open('vehicles-location.json') as myfile:
    vehicle_data=[myfile.read()]

dict(vehicle_data)
map = folium.Map(vehicle_data.value("001078f6-acfd-42fe-8c9c-84cecbb83630", 'location'))
map.save('html')
class Vehicle:
    def __init__():
        id=

    def