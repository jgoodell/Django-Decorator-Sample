from django.http import HttpResponse
from django.shortcuts import render

from geotools import (fetch_data,
                      STATES,
                      )
def index(request):
    return render(request, 'geodata/index.html', {'states':STATES})
