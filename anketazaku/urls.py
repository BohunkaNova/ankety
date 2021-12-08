
from django.urls import path

from .import views, blabol

urlpatterns = [
    path('', views.index, name='index'),
    path('blabol', blabol.index, name='blabo'),

]

