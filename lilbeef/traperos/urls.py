'''
 Este fichero no es por defecto de Django, pero nos ayuda a separar el routing por aplicaciones que conforman
 un proyecto.

 De modo que definimos para esta app las rutas que son exclusivamente suyas y luego las importamos en el router
 principal del proyecto
'''

from django.urls import path
from traperos import views

urlpatterns = [
    path('', views.index),
    path('traperos/', views.traperos_lista),
    path('traperos/<int:trapero_id>', views.traperos_id),
    path('discos/', views.disco_lista),
    path('discos/<int:disco_id>', views.disco_id),
    path('tiraeras/', views.tiraeras_lista),
    path('tiraeras/<int:tiraera_id>', views.tiraeras_id),
]