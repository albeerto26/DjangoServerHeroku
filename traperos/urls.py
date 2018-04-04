"""
Fichero para separar routing por aplicacionesun proyecto.

De modo que definimos para esta app las rutas que son exclusivamente suyas y luego las importamos en el router
principal del proyecto.
"""

from django.urls import path
from traperos import views

urlpatterns = [
    path('', views.index, name='index'),
    path('respuesta/', views.respuesta_simple, name='respuesta'),
    path('traperos/', views.traperos_lista, name='traperos'),
    path('traperos/<int:trapero_id>', views.traperos_id, name='trapero_id'),
    path('discos/', views.DiscoListView.as_view(), name='discos'),
    path('discos/<int:pk>', views.DiscoDetailView.as_view(), name='disco_id'),
    path('tiraeras/', views.tiraeras_lista, name='tiraeras'),
    path('tiraeras/<int:tiraera_id>', views.tiraeras_id, name='tiraera_id'),
    path('tiraeras_trapero/<int:trapero_id>', views.tiraeras_trapero, name='tiraeras_trapero'),
    path('alertas/', views.AlertaCreate.as_view(), name='alertas'),
    path('alertas/gracias/', views.AlertaGraciasView.as_view(), name='alertas'),
    path('fin/', views.FinView.as_view(), name='fin'),
]
