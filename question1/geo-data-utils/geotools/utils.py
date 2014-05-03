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

def fetch_json(uri, state, method="GET"):
    '''Fetches the provided state data and returns pretty JSON formatted string..

    Arguments:
    uri:        The URI as a string to the API that serves the geo location data.
    state:      Two capital letter state abbreviation, e.g. CA for California.

    Keyword Arguments:
    method:     The HTTP method to use in the request to the API.

    Raises:
    ValueError: If you supply an invalid state abbreviation.
    gaierror/CannotSendRequest: If there is no network connection.
    '''
    state = state.lower()
    CONNECTION.request(method, uri % state)
    response = CONNECTION.getresponse()
    json_data = json.loads(response.read())
    json_data = json.dumps(json_data, sort_keys=True,
                           indent=4, separators=(',', ': '))
    CONNECTION.close()
    return json_data

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
    

