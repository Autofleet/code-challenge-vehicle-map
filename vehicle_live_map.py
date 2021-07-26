import json
import folium
import http.server
import socketserver
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast


def main():
    global vehicle_ids
    global vehicle_data
    global map
    with open('vehicles-location.json') as myfile:
         vehicle_data=json.load(myfile)
    crucial_car_data=get_ids_locations(vehicle_data)
    vehicle_coordinates=get_lats_lngs(crucial_car_data[1])
    vehicle_ids=crucial_car_data[0]
    dict_of_ids_locations={}
    for lat, lng, id in zip(vehicle_coordinates[0], vehicle_coordinates[1], vehicle_ids):
        dict_of_ids_locations[id]=[lat, lng]

    map=folium.Map(location=(51.5074, 0.1278), tiles="Stamen Terrain")
    fg=folium.FeatureGroup(name="vehicle_map")
    
    for lat, lng, id in zip(vehicle_coordinates[0], vehicle_coordinates[1], vehicle_ids):
        fg.add_child(folium.Marker(location=[lat, lng], popup=id, icon=folium.Icon(color='green')))
    map.add_child(fg)
    map.save("london.html")
    PORT=8080
    Handler=http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print ("serving at port", PORT)
        httpd.serve_forever()




    

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