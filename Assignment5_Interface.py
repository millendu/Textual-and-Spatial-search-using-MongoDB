#!/usr/bin/python2.7
#
# Assignment5 Interface
# Name: MANIDEEP ILLENDULA
# ID: 1208825003

from pymongo import MongoClient
import os
import sys
import math
import json
import re

def FindBusinessBasedOnCity(cityToSearch, saveLocation1, collection):
    f = open(saveLocation1, 'w')
    cityToSearch = cityToSearch.strip()
    if(len(cityToSearch) == 0):
        return
    for a in collection.find({'city' : re.compile(cityToSearch, re.IGNORECASE)}, {'name' : 1 , 'full_address' : 1 , 'city' : 1 , 'state' : 1, '_id' : 0}):
        s =  a['name'] + "$" + a['full_address'].replace("\n", " ") + "$" + a['city'] + "$" + a['state']
        f.write(s.encode("utf-8").upper() + "\n")

def FindBusinessBasedOnLocation(categoriesToSearch, myLocation, maxDistance, saveLocation2, collection):
    f = open(saveLocation2, 'w')
    for a in collection.find({'categories' : {'$in' : categoriesToSearch}}):
        lat1 = float(a['latitude'])
        lon1 = float(a['longitude'])
        lat2 = float(myLocation[0])
        lon2 = float(myLocation[1])
        if(dist(lat1, lon1, lat2, lon2) <= maxDistance):
            f.write((a['name']).encode("utf-8").upper() + "\n")

def dist(lat1, lon1, lat2, lon2):
    dlon = math.radians(lon2) - math.radians(lon1)
    dlat = math.radians(lat2) - math.radians(lat1)
    a = math.pow((math.sin(dlat/float(2))),2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.pow(math.sin(dlon/float(2)),2)
    c = 2 * math.atan2( math.sqrt(a), math.sqrt(1-a) )
    dist = 3959 * c
    return dist
