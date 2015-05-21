import yaml
import requests

# The name of the API key token that must be in secrets.yml
API_KEY_PATH = "geolocation_api_key"

GOOGLE_MAPS_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

class GeolocateFailure(Exception):
    pass

def geolocate(config, address):
    # convert address to lat-longs

    # fetch from google api
    api_key = config[API_KEY_PATH]
    payload = { "address": address, "key": api_key }
    result = requests.get(GOOGLE_MAPS_URL, params = payload)

    # interpret results
    result_object = result.json()
    result_results = result_object["results"]
    if len(result_results) < 1:
        raise GeolocateFailure("Could not find a single result for address '{}'" % address)

    # grab first geometry result to extract lat-long
    result_geometry = result_results[0]["geometry"]
    latlong = result_geometry["location"]

    # This is separated to try and insulate the downstream code
    # from any changes Google might make.
    return { "lat": latlong['lat'], "long": latlong['lng'] }
    
def configure(secretsFilePath):
    # load from config
    with open(secretsFilePath, 'rb') as fp:
        config = yaml.load(fp)
        return config
        
if __name__ == '__main__':
    config = configure('secrets.yml')
    ll = geolocate(config, '1600 pennsylvania avenue washington dc')
    print ll