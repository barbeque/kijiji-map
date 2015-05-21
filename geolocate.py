import yaml
import requests

# The name of the API key token that must be in secrets.yml
API_KEY_PATH = "geolocation_api_key"

GOOGLE_MAPS_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

def geolocate(config, address):
    # convert address to lat-longs
    api_key = config[API_KEY_PATH]
    payload = { "address": address, "key": api_key }
    result = requests.get(GOOGLE_MAPS_URL, params = payload)
    print result.json()
    
def configure(secretsFilePath):
    # load from config
    with open(secretsFilePath, 'rb') as fp:
        config = yaml.load(fp)
        return config
        
if __name__ == '__main__':
    config = configure('secrets.yml')
    geolocate(config, '1600 pennsylvania avenue washington dc')