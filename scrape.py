# Script to scrape ECan webportal for freshwater consents
# Author: R. Peer
# Contributors: N. Cameron & O. Saunders

#import packages
import pandas as pd
import requests
import urllib.request

#test with one consent number
consent = 'CRC165168' #groundwater

#load url
url = 'https://data.ecan.govt.nz:443/data/154/Water/Water%20permit%20use/CSV?ConsentNo='+consent
r = requests.get(url)

testdf = pd.read_csv(url)

#check response for errors
#print(r.status_code) #200 = request success

data = r.text

gw_consents = pd.Dataframe()
