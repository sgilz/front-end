from django.shortcuts import render, HttpResponse
import requests

# Create your views here.

def measure(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        lat = request.GET['latitude']
        length = request.GET['length']
        ground  = request.GET['grounds']
        # Verifica si el value no esta vacio
        if value and lat and length and ground:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': 'ph', 'value': value, 'latitude': lat, 'length' : length, 'ground': ground}
            response = requests.post("http://pi1-eafit-sgilz.azurewebsites.net/hygrometer/", args)
            # Convierte la respuesta en JSON
            measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get("http://pi1-eafit-sgilz.azurewebsites.net/hygrometer/")
    # Convierte la respuesta en JSON
    measures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "measure/measure.html", {'measures': measures})


