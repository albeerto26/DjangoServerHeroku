from django.http import HttpResponse
from django.shortcuts import render

from traperos.models import Trapero, Disco, Tiraera

# Create your views here.

def index(request):
    #return HttpResponse("Bienvenido a Lil Beef")
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #context = {'latest_question_list': latest_question_list}
    context = {}
    return render(request, 'index/index.html', context)


def traperos_lista(request):
    listado_todos_traperos = Trapero.objects.all()
    context = {'listado_todos_traperos': listado_todos_traperos}
    return render(request, 'traperos/listado_todos_traperos.html', context)

def traperos_id(request, trapero_id):
    unico_trapero = Trapero.objects.get(id=trapero_id)
    context = {'unico_trapero': unico_trapero}
    return render(request, 'traperos/unico_trapero.html', context)

def disco_lista(request):
    listado_todos_discos = Disco.objects.all()
    context = {'listado_todos_discos': listado_todos_discos}
    return render(request, 'discos/listado_todos_discos.html', context)

def disco_id(request, disco_id):
    unico_disco = Disco.objects.get(id=disco_id)
    context = {'unico_disco': unico_disco}
    return render(request, 'discos/unico_disco.html', context)

def tiraeras_lista(request):
    listado_todas_tiraeras = Tiraera.objects.all()
    context = {'listado_todas_tiraeras': listado_todas_tiraeras}
    return render(request, 'tiraeras/listado_todas_tiraeras.html', context)

def tiraeras_id(request, tiraera_id):
    unica_tiraera = Tiraera.objects.get(id=tiraera_id)
    context = {'unica_tiraera': unica_tiraera}
    return render(request, 'tiraeras/unica_tiraera.html', context)
