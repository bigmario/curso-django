from django.http import HttpResponse

from datetime import datetime

from django.http.request import HttpRequest
from django.http import JsonResponse

def hola_mundo(request):
    now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')
    return HttpResponse(f"Hi, the time is {now}")


def sort_integers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]

    numbers = sorted(numbers)

    data = {
        'status': 'ok',
        'numbers': numbers,
        'message': 'Integers sorted succesfully'
    }

    return JsonResponse(data,  json_dumps_params={'indent': 4}, safe=False)

def verificar_edad(request, name, edad):
    if edad >= 18:
        status = 'Ok'
        message = f'Bienvenido, {name.capitalize()}, eres mayor de edad'
    else:
        status = 'Error'
        message = f'{name.capitalize()}, No tienes permitido el acceso, eres menor de edad'

    data = {
            'status': status,
            'message': message
    }

    return JsonResponse(data,  json_dumps_params={'indent': 4}, safe=False)