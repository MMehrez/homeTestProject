"""
Created on Tue Apr 03 19:09:37 2018
@author: Mohamed W. Mehrez Said
email: m.mehrez.said@mun.ca
"""
import time
import requests

if __name__ == '__main__':
    # welcome and information message
    print ("Welcome to HOME-TEST Geocoding Service!")
    print ("This service returns the latitude and longitude coordinates for (a) given address(es).")       
 
    time.sleep(1)
    input("Press Enter to continue...")
    
    # address request message
    requested_addresses = input('Enter the Address(es) separated by a (;)')
    requested_addresses = requested_addresses.split(";")

    url_google = 'https://maps.googleapis.com/maps/api/geocode/json'
    url_here = 'https://geocoder.cit.api.here.com/6.2/geocode.json'

    i = 0;
    while i < len(requested_addresses):
        location = geocodingGoogle(i,url_google)
        if location == 'Error':
            location = geocodingHere(i,url_here)
        print ("The coordinates of",requested_addresses[i],"are: latitude:",location['lat'],"and longitude:",location['lng'])
        i+=1

def geocodingGoogle(index,url):
    try:
        params = {'address': requested_addresses[index]}
        r = requests.get(url, params=params)
        results = r.json()
        location = results['results'][0]['geometry']['location']
        return location
    except:        
        location = 'Error'
        return location

def geocodingHere(index,url):
    try:
        params = {'searchtext': requested_addresses[index],'app_id':'ZuuaESOoZ3r0TfUpSNLN','app_code':'cNeC1goF-_A2H5Zbth4vmQ'}
        r = requests.get(url, params=params)
        results = r.json()
        location = results['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']        
        location = {'lat': location['Latitude'], 'lng': location['Longitude']}
        return location
    except:        
        location = {'lat': 'Error', 'lng': 'Error'}
        return location            