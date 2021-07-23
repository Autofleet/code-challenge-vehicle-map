
import json
import folium
def main():
    with open('vehicles-location.json') as myfile:
        vehicle_data=[myfile.read()]
    print(get_ids_locations(vehicle_data))
#for i in vehicle_data:
#    map = folium.Map(vehicle_data.value("001078f6-acfd-42fe-8c9c-84cecbb83630", 'location'))
#map.save('html')



def get_ids_locations(list_of_dicts):
    ids=[]
    latitudes=[]
    longitudes=[]
    for i in list_of_dicts:
        for key, value in list_of_dicts.items():
            if type(value) is dict and key=="location":
                get_ids_locations(value)
            else:
                if key=="lat":
                    latitudes.append(value)
                elif key=="lng":
                    longitudes.append(value)
                elif key=="id":
                    ids.append(value)
    return ids, latitudes, longitudes
