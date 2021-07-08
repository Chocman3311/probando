from django.urls import path
from django.urls.resolvers import URLPattern
from .views import index, trabajos, acercade, formulario, api

urlpatterns = [
    path('', index,name="index"),
    path('trabajos/',trabajos,name="trabajos"),
    path('acercade/',acercade,name="acercade"),
    path('formulario/',formulario,name="formulario"),
    path('api/',api,name="api")
]