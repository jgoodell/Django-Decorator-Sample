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

if __name__ == "__main__":
    from pprint import pprint
    from optparse import OptionParser as P
    
    connection = HTTPConnection(HOST, 80)

    for state in STATES:
        state = state.lower()
        json_file = open("data/%s.json" % state, 'w')
        connection.request("GET", URI % state)
        response = connection.getresponse()
        json_data = json.loads(response.read())
        json_file.write(json.dumps(json_data, sort_keys=True,
                                   indent=4, separators=(',', ': ')))
        json_file.close()
        connection.close()
