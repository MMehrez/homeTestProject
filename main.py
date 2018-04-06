# -*- coding: utf-8 -*-
"""
Created on Tue Apr 03 19:09:37 2018
@author: Mohamed W. Mehrez Said
email: m.mehrez.said@mun.ca
Description: This program is a simple network service that returns latitude and longitude coordinates 
of a give address or a list of addresses.
Run this program using python version 3.0 or newer versions.
"""
import urllib.request, urllib.parse
import json, time

# google geocoding function
def geocodingGoogle(requested_address):
    url_google = 'https://maps.googleapis.com/maps/api/geocode/json?' #google main url for geocoding requests
    params = {'address': requested_address}
    req_url = url_google + urllib.parse.urlencode(params)
    try:
        response = urllib.request.urlopen(req_url)
        data = response.read().decode()
        results = json.loads(data)
        location = results['results'][0]['geometry']['location']
    except:
        location = 'Error'
    return location

# google geocoding function
def geocodingHere(requested_address):
    url_here = 'https://geocoder.cit.api.here.com/6.2/geocode.json?'  #Here main url for geocoding requests
    params = {'searchtext': requested_address,'app_id':'ZuuaESOoZ3r0TfUpSNLN',\
              'app_code':'cNeC1goF-_A2H5Zbth4vmQ'}
    req_url = url_here + urllib.parse.urlencode(params)
    try:
        response = urllib.request.urlopen(req_url)
        data = response.read().decode()
        results = json.loads(data)
        location = results['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']        
        location = {'lat': location['Latitude'], 'lng': location['Longitude']}
    except:
        location = {'lat': 'Error', 'lng': 'Error'}
    return location    


if __name__ == '__main__':
    # welcome and information message
    print ("Welcome to HOME-TEST Geocoding Service!")
    print ("This service returns the latitude and longitude coordinates for (a) given address(es).")       
    time.sleep(1)
    input("Press Enter to continue...")
    
    # address request message
    requested_addresses = input('Enter the Address(es) separated by a (;)')
    requested_addresses = requested_addresses.split(";")
      
    i = 0;
    while i < len(requested_addresses):
        location = geocodingGoogle(requested_addresses[i])#primary geocoding service (google)
        if location == 'Error':
            location = geocodingHere(requested_addresses[i]) #Secondary geocoding service (Here)
        print ("The coordinates of",requested_addresses[i],"are: (latitude:",\
               location['lat'],")","and (longitude:",location['lng'],")")
        i+=1