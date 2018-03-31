"""Gestion de respuestas HTTP."""
from django.http import HttpResponse
"""Shortcut para crear respuestas HTTP elaboradas."""
from django.shortcuts import render
"""Importacion para generic Views List."""
from django.views.generic.list import ListView
"""Importacion para generic Views Detail."""
from django.views.generic.detail import DetailView
"""Importacion de modelos a usar en la aplicacion."""
from django.views.generic.edit import CreateView
"""Importacion de vistas genericas a traves de plantillas."""
from django.views.generic.base import TemplateView
"""Importacion de vista de creacion usada en  Alertas."""
from traperos.models import Trapero, Disco, Tiraera, Alerta

# Create your views here.

def respuesta_simple(request):
    """Ejemplo de respuestas simple."""
    return HttpResponse("Bienvenido a Lil Beef")


def index(request):
    """Vista para mostrar el indice de la aplicacion."""
    traperos = Trapero.objects.all().order_by('?')[:2]
    discos = Disco.objects.order_by('-fecha_publicacion')[:2]
    tiraeras = Tiraera.objects.order_by('-fecha_inicio')[:2]
    context = {'traperos': traperos, 'discos': discos, 'tiraeras': tiraeras}
    return render(request, 'index/index.html', context)


def traperos_lista(request):
    """Listado de traperos."""
    listado_todos_traperos = Trapero.objects.all()
    context = {'listado_todos_traperos': listado_todos_traperos}
    return render(request, 'traperos/listado_todos_traperos.html', context)


def traperos_id(request, trapero_id):
    """Muestra un unico trapero."""
    unico_trapero = Trapero.objects.get(id=trapero_id)
    context = {'unico_trapero': unico_trapero}
    return render(request, 'traperos/unico_trapero.html', context)


class DiscoListView(ListView):
    """ListView Disco"""
    model = Disco
    template_name = 'discos/listado_todos_discos.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'listado_todos_discos'  # Default: object_list
    paginate_by = 3
    queryset = Disco.objects.all()  # Default: Model.objects.all()


class DiscoDetailView(DetailView):
    """DetailView Disco"""
    model = Disco
    template_name = 'discos/unico_disco.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'unico_disco'  # Default: object_list


def tiraeras_lista(request):
    """Listado de tiraeras."""
    listado_todas_tiraeras = Tiraera.objects.all()
    context = {'listado_todas_tiraeras': listado_todas_tiraeras}
    return render(request, 'tiraeras/listado_todas_tiraeras.html', context)


def tiraeras_id(request, tiraera_id):
    """Muestra una unica tiraera."""
    unica_tiraera = Tiraera.objects.get(id=tiraera_id)
    context = {'unica_tiraera': unica_tiraera}
    return render(request, 'tiraeras/unica_tiraera.html', context)

def tiraeras_trapero(request, trapero_id):
    """Muestra una unica tiraera."""
    listado_todas_tiraeras = Tiraera.objects.filter(trapero_tira__pk=trapero_id)
    context = {'listado_todas_tiraeras': listado_todas_tiraeras}
    return render(request, 'tiraeras/listado_todas_tiraeras.html', context)


class AlertaCreate(CreateView):
    """Vista de creacion de Alertas"""
    model = Alerta
    template_name = 'alertas/alertas_form.html'
    success_url = '/alertas/gracias'
    fields = ['titulo', 'descripcion', 'trapero', ]


class AlertaGraciasView(TemplateView):
    """Vista de agradecimiento por envio de Alertas"""
    template_name = 'alertas/alertas_gracias.html'
