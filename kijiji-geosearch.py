import geolocate
import get_addresses
import sys
import getopt

def main(argv):
    # Get command-line arguments.   
    rss_path = 'trucks.rss'
    my_address = '140 15 Ave NW, calgary, ab'

    try:
        opts, args = getopt.getopt(argv, "a:f", ["feed=", "address="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-a', '--address'):
            my_address = arg
        elif opt in ('-f', '--feed'):
            rss_path = arg
    print 'RSS path {}'.format(rss_path)
    print 'My address {}'.format(my_address)

    # Download my lat-long from geolocation

    # Parse the trucks RSS into objects I can use

    # Scan through the trucks RSS and geolocate (maybe with a cache, this is
    # a lot of requests...)

    # Return the RSS items that geolocate to pretty close to the lat-long
    # in my address.

if __name__ == '__main__':
    main(sys.argv[1:])
