from django.http import HttpResponse
from django.shortcuts import render

from geotools import (fetch_json,
                      URI,
                      STATES,
                      )
def index(request):
    '''View that supplies the site index, links on this page allow you to
    navigate the remainder of the site.
    '''
    if request.method == 'GET':
        return render(request, 'geodata/index.html', {'states':STATES, 'uri':'geodata/'})
    else:
        response = HttpResponse("405 Method Not Allowed")
        response.status_code = 405
        return response

def data(request, state):
    '''View that gets the geo location date for a specific state.
    '''
    if request.method == 'GET':
        try:
            data = fetch_json(URI,state)
        except ValueError:
            response = HttpResponse("400 Bad Request")
            response.status_code = 400
            return response
        return HttpResponse(data)
    else:
        response = HttpResponse("405 Method Not Allowed")
        response.status_code = 405
        return response
