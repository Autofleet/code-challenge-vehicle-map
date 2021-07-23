import json
import folium

def main():
    with open('vehicles-location.json') as myfile:
        vehicle_data=json.load(myfile)
    print(len(vehicle_data))
    crucial_car_data=get_ids_locations(vehicle_data)
    vehicle_coordinates=get_lats_lngs(crucial_car_data[1])
    map=folium.Map(location=(51.5074, 0.1278), tiles="Stamen Terrain")
    map.save("london.html")
    fg=folium.FeatureGroup(name="vehicle_map")
    #for coordinates in 





def get_ids_locations(list_of_dicts):
    ids=[]
    locations=[]
    for d in list_of_dicts:
        if type(d)==dict:
            for key, value in d.items():
                if key=="location":
                    locations.append(value)
                else: 
                    if key=="id":
                        ids.append(value)
    return ids, locations
def get_lats_lngs(list_of_dicts):
    latitudes=[]
    longitudes=[]
    for d in list_of_dicts:
        for k, v in d.items():
            if k=="lat":
                latitudes.append(v)
            elif k=="lng":
                longitudes.append(v)
    return latitudes, longitudes
main()