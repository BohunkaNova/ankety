
from django.urls import path

from .import views, blabol

urlpatterns = [
    path('', views.index, name='index'),
    path('blabol', blabol.index, name='blabo'),
    path('list/', views.list, name='list'),
    path('tmp/', views.tmp, name='tmp'),
    path('<int:question_id>/', views.detail, name='detail'),

]

