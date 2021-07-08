from django.urls import path
from django.urls.resolvers import URLPattern
from .views import index, trabajos

urlpatterns = [
    path('', index,name="index"),
    path('trabajos/',trabajos,name="trabajos")
]