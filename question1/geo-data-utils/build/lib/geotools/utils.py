'''Module to fetch geolocation data from

    http://api.sba.gov/geodata/city_county_links_for_state_of/in.json

and process the data as outlined in software_engineer_test.txt.

This module can also be executed as a script, a help message will print
with directions on how to use the script.
'''
import json
from httplib import HTTPConnection

STATES = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
    ]

HOST = "api.sba.gov"

URI = "/geodata/city_county_links_for_state_of/%s.json"

CONNECTION = HTTPConnection(HOST, 80)

def fetch_data(uri, state, file_name, file_uri=None):
    '''Fetches the provided state data and places the data in a specified file.

    Arguments:
    state:      Two capital letter state abbreviation, e.g. CA for California.
    file_name:  A string indicating the name of the file to place the data in.

    Optional Arguments
    file_uri:   The location to place the file at, default is the current directory.
    '''
    state = state.lower()
    try:
        json_file = open(file_uri + '/' + file_name, 'w')
    except TypeError:
        json_file = open(file_name, 'w')
    CONNECTION.request("GET", uri % state)
    response = CONNECTION.getresponse()
    json_data = json.loads(response.read())
    json_file.write(json.dumps(json_data, sort_keys=True,
                               indent=4, separators=(',', ': ')))
    json_file.close()
    CONNECTION.close()
    

if __name__ == "__main__":
    import sys
    import os
    from optparse import OptionParser as P
    p = P(description="Fetches geolocation data by state from api.sba.gov.",
          version='0.1-alpha',
          prog=os.path.basename(__file__),
          usage="python %prog [options]",
          epilog="This file can also be used as a module.")
    p.add_option('-v', '--verbose', action='store_true', dest="verbose",
                 help='Will print out the state currently being fetched to stdout.')
    p.add_option('-S', '--state', action='store', dest='state',
                 help='Select a state to fetch geolocation data about using the two capital letter abbreviation, e.g. CA for California.')
    opts, args = p.parse_args()

    if opts.state:
        if opts.verbose: print("Fetching %s..." % opts.state)
        try:
            fetch_data(URI, opts.state, '%s.json' % opts.state, file_uri='data')
        except ValueError:
            print("Error: '%s' is not a valid state abbreviation." % opts.state)
            sys.exit(1)
        except Exception, e:
            print("Error: Check your internet connection.")
            sys.exit(1)
        sys.exit(0)
    else:
        print('here')
        for state in STATES:
            if opts.verbose: print("Fetching %s..." % state)
            try:
                fetch_data(URI, state, '%s.json' % state, file_uri='data')
            except:
                print("Error: Check your internet connection.")
                sys.exit(1)
        sys.exit(0)
