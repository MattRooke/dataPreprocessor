# A simple script for converting Google takeout location data .json files to .csv

import csv
import json

from xlwings import xrange

# id of file being converted:
ID = "#"

# .json file location:
fileName = 'locationHistory' + ID + '.json'

# read json file
print('reading file')
file = open(fileName, "r")
content = file.read()
file.close()
print('success!')

# read json
print('loading json')
data = json.loads(content)
print('success!')

# create file
print('creating csv')
fieldnames = ["Id", "Latitude", "Longitude", "Date"]
w = open('history' + ID + '.csv', 'w', newline='')
wr = csv.writer(w, delimiter=',')
wr.writerow(fieldnames)

count = len(data['locations'])

for c in xrange(0, count):

    # convert current location to standard latitude/longitude
    latitude = float(data['locations'][c]['latitudeE7']) / 10000000
    longitude = float(data['locations'][c]['longitudeE7']) / 10000000
    # convert time stamp from mills to date
    time = float(data['locations'][c]['timestampMs'])

    # get next location, except if this is the last of the list
    if c < count - 1:
        nextLat = float(data['locations'][c + 1]['latitudeE7']) / 10000000
        nextLong = float(data['locations'][c + 1]['longitudeE7']) / 10000000
    else:
        nextLat = latitude
        nextLong = longitude

    # Id(person), Lat, Long, Date
    output = [ID, str(latitude), str(longitude), str(time)]
    wr.writerow(output)
    print('progress: ' + str(c) + '/' + str(count))

w.close()
print('finished successfully!')
