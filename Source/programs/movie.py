# coding=utf-8
# python 3

# Import required classes
import json
import urllib.request
import urllib.parse
import datetime

API_KEY = 'f9a00520ec2beacdec7f69bf6a20d085'

request = input('Filmtitel eingeben: ')

# Get the json file from the API
url = 'http://api.themoviedb.org/3/search/movie?api_key=' + API_KEY + '&query=' + urllib.parse.quote(request, safe='')
raw_answer = urllib.request.urlopen(url)

# Parse the json
answer = json.load(raw_answer)

# Display all movies foound
results = answer['results']
index = 0
for movie in results:
    id = movie['id']
    title = movie['title']
    original_title = movie['original_title']
    release_date = movie['release_date']
    print(str(index) + ' ' + title + ' (' + original_title + ')' + ' ' + release_date)
    index +=1

print('')

# Request details
index = int(input('Index of the film for details: '))

# Get the json file from the API
url = 'http://api.themoviedb.org/3/movie/' + str(results[index]['id']) + '?api_key=' + API_KEY
raw_details = urllib.request.urlopen(url)

# Parse the json
details = json.load(raw_details)

print('')

print(details['overview'])

print('')

print('Ort:')
for country in details['production_countries']:
    print('   ' + country['name'])

print('')

print('Genres:')
for genre in details['genres']:
    print('   ' + genre['name'])

print('')

print('Sprachen:')
for language in details['spoken_languages']:
    print('   ' + language['name'])

print('')

print('Runtime: ' + str(details['runtime']))