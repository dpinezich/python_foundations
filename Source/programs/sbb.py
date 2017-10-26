# coding=utf-8

# Import required classes
import json
from urllib import quote
import urllib2
import datetime

request = raw_input('gewünschte Station eingeben: ')

# Get the json file from the API
raw_answer = urllib2.urlopen('http://transport.opendata.ch/v1/stationboard?station=' + quote(request) + '&limit=10')

# Parse the json
answer = json.load(raw_answer)

# Display station information
print('Folgende Station wurde gefunden: ' + answer['station']['name'])

# Display all available connections from this station
connections = answer['stationboard']
for connection in connections:
    name = connection['name']
    category = connection['category']
    to = connection['to']
    departure_time = datetime.datetime.strptime(connection['stop']['departure'][:-5], '%Y-%m-%dT%H:%M:%S')
    in_minutes = int((departure_time - datetime.datetime.now()).total_seconds() / 60)
    print(category + u' (' + name + u')' + u' fährt in ' + str(in_minutes) + u' Minuten nach ' + to)
