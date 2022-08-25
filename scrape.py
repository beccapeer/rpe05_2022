# Script to scrape ECan webportal for freshwater consents
# Author: R. Peer
# Contributors: N. Cameron & O. Saunders

#import packages
import pandas as pd
import requests

#set empty dataframe for data collection
w_df = pd.DataFrame()

#load consent numbers
consents_df = pd.read_csv('./data/consent-numbers-ECan.csv')
consents = consents_df["Number"]

for i in consents:
    url = 'https://data.ecan.govt.nz:443/data/154/Water/Water%20permit%20use/CSV?ConsentNo='+i

    #catch any errors
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as e:  
        raise SystemExit(e)
    
    #pull data
    w_data = pd.read_csv(url)
    
    #store in dataframe
    w_df = w_df.append(w_data)

#save scraped data
w_df.to_csv('./data/ECan_water_consent_data_raw.csv')