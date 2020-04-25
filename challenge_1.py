# CHALLENGE PROBLEMS
# YOU MAY NOT USE ANY ADDITIONAL LIBRARIES OR PACKAGES TO COMPLETE THIS CHALLENGE

# Divvy is Chicago's bike share system, which consists of almost 600 stations scattered
# around the city with blue bikes available for anyone to rent. Users begin a ride by removing
# a bike from a dock, and then they can end their ride by returning the bike to a dock at any Divvy 
# station in the city. You are going to use real data from Divvy collected at 1:30pm on 4/7/2020 
# to analyze supply and demand for bikes in the system. 

# NOTE ** if you aren't able to run this, type "pip install json" into your command line
import os
os.system('cls' if os.name=='nt' else 'clear')
"""clear console"""

import json
import requests

# do not delete; this is the data you'll be working with
#divvy_stations = json.loads(open('/Users/marksheppard/Documents/GitHub/PythonCourse/Harris-Challenge-1/divvy_stations.txt').read())

gbfs_resp = requests.get('https://gbfs.divvybikes.com/gbfs/fr/station_status.json')
gbfs_json = json.loads(gbfs_resp.text)

divvy_stations_ = gbfs_json['data']['stations']


# PROBLEM 1
# find average number of empty docks (num_docks_available) and 
# available bikes (num_bikes_available) at all stations in the system

result_docks = []
result_bikes = []
result_rented = []
result_e_bikes = []

for data in divvy_stations_:
    result_docks.append(data['num_docks_available'])
    result_bikes.append(data['num_bikes_available'])
    result_rented.append(data['is_renting'])
    result_e_bikes.append(data['num_ebikes_available'])

def average_():
    av_dock = sum(result_docks)/len(result_docks)
    av_bike = sum(result_bikes)/len(result_bikes)
    print("The average number of docks available is: ~%.2f" % av_dock)
    print("The average number of bikes available is: ~%.2f" % av_bike)
average_()

# PROBLEM 2
# find ratio of bikes that are currently rented to total bikes in the system (ignore ebikes)

def ratio_():
    ratio_rented = sum(result_rented)*100/sum(result_bikes)-sum(result_e_bikes)
    print("The ratio of bikes currently being rented is: ~%.2f" % ratio_rented + "%")
ratio_()


# PROBLEM 3 
# Add a new variable for each divvy station's entry, "percent_bikes_remaining", that shows 
# the percentage of bikes available at each individual station (again ignore ebikes). 
# This variable should be formatted as a percentage rounded to 2 decimal places, e.g. 66.67%

def available():
    ratio_rented = 100 - (sum(result_rented)*100/sum(result_bikes)-sum(result_e_bikes))
    print("The ratio of bikes currently available is: ~%.2f" % ratio_rented + "%")
available()