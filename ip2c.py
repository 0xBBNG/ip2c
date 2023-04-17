import pandas as pd
import geoip2.database

# read CSV file
df = pd.read_csv('input.csv')

# load GeoIP2 database
reader = geoip2.database.Reader('GeoLite2-Country.mmdb')

# define function to get country from IP address
def get_country(ip_address):
    try:
        response = reader.country(ip_address)
        country = response.country.name
    except:
        country = ''
    return country

# add new column for country data
df['country'] = ''

# loop through each row in the dataframe and get country data
for index, row in df.iterrows():
    ip_address = row['ip_address']
    country = get_country(ip_address)
    df.at[index, 'country'] = country

# save data to Excel file
df.to_csv('output.csv', index=False)