This relies heavily on BeautifulSoup, which I did not write. Thanks though, best library ever!

# To Use

## Install requirements with pip
Once you have pip installed, install the third party library requirements with `pip install -r requirements.txt`.

## Create secrets.yml file
Create a file named `secrets.yml` in the same directory as the python script.

It should have the following keys:

 * `geolocation_api_key`: Your Google Geocoding "server side" API key. You can generate a new one [here](https://console.developers.google.com//flows/enableapi?apiid=geocoding_backend&keyType=SERVER_SIDE)

## Download kijiji RSS

 1. Run a search in kijiji
 2. Copy the RSS link at the lower right of the results screen.
 3. Use curl or wget to copy that RSS link to a local file (e.g. `trucks.rss`)

## Run the application
TODO: Not implemented yet.
