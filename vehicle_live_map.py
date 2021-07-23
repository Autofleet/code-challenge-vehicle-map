import json
import folium
from folium.map import Icon, Popup

def main():
    with open('vehicles-location.json') as myfile:
        vehicle_data=json.load(myfile)
    #print(len(vehicle_data))
    crucial_car_data=get_ids_locations(vehicle_data)
    vehicle_ids=crucial_car_data[0]
    vehicle_coordinates=get_lats_lngs(crucial_car_data[1])
    map=folium.Map(location=(51.5074, 0.1278), tiles="Stamen Terrain")
    fg=folium.FeatureGroup(name="vehicle_map")
    
    index=0
    for lat, lng in zip(vehicle_coordinates[0], vehicle_coordinates[1]):
        fg.add_child(folium.Marker(location=[lat, lng], Popup=vehicle_ids[index], icon=folium.Icon(color='green')))
        index+=1
    map.add_child(fg)
    map.save("london.html")





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
    #coordinates=[{latitudes[i]: longitudes[i] for i in range(len(latitudes))}]
    return latitudes, longitudes
main()