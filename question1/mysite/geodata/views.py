import json

from django.http import HttpResponse
from django.shortcuts import render

from geotools import (fetch_json,
                      URI,
                      STATES,
                      )

ERROR_400 = "400 Bad Request"
ERROR_404 = "404 Not Found"
ERROR_405 = "405 Method Not Allowed"
ERROR_500 = "500 Server Error"

def index(request):
    '''View that supplies the site index, links on this page allow you to
    navigate the remainder of the site.

    Arguments:
    request:  HttpRequest instance.
    '''
    if request.method == 'GET':
        return render(request, 'geodata/index.html', {'states':STATES})
    else:  # Only accept requests via the GET method.
        response = HttpResponse(ERROR_405)
        response.status_code = 405
        return response

def all_data(request):
    '''View that gets the geo locationdata for all states.

    Arguments:
    request:  A HttpRequest instance.
    '''
    if request.method == 'GET':
        return HttpResponse('{message:"Hello world!"}',content_type="application/json")        
    else:
        response = HttpResponse(ERROR_405)
        response.status_code = 405
        return response

def data(request, state):
    '''View that gets the geo location date for a specific state.

    Arguments:
    request:  A HttpRequest instance.
    state:    String two letter state abbreviation.
    '''
    if request.method == 'GET':
        try:
            data = fetch_json(URI,state)
        except ValueError:  # A value error is raised if the URI is invalid.
            response = HttpResponse(ERROR_400)
            response.status_code = 400
            return response
        except Exception, e:
            # This is most likely a network problem on the server.
            response = HttpResponse(ERROR_500 + ": " + str(type(e)) + " " + str(e))
            response.status_code = 500
            return response
        return HttpResponse(data,content_type="application/json")
    else:  # Only accept request via the GET method.
        response = HttpResponse(ERROR_405)
        response.status_code = 405
        return response
