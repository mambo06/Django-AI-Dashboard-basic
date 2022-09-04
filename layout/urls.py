from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('datatables',views.datatables,name='datatables'),
    path('charts', views.charts, name='charts'),
    path('menu', views.menu, name='menu'),
    path('sgd', views.sgd, name='sgd'),
    path('cs', views.chartJs, name='chartsSample'),
    path('choropleth', views.choropleth, name='Choropleth'),
    path('bubblemap', views.bubblemap, name='bubleMap'),
    path('mapamcharts', views.mapamcharts, name='mapsAmcharts')

]