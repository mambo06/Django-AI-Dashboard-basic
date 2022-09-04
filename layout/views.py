from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import context
from . import chartsSample as cs
from .fig_code import sgd_separator
import numpy as np
import json




def index(request):
    return render(request, 'layout/index.html')

def datatables(request):
    return render(request, 'layout/datatables.html')

def charts(request):
    return render(request, 'layout/charts.html')

def menu(request):
    return render(request, 'layout/menu.html')

def sgd(request):
    graphic = sgd_separator.plot_sgd_separator()
    return render(request, 'layout/sgd.html',{'graphic':graphic})

def chartJs(request):
    data = []
    tipe = ['bubble','line','scatter']
    for i in range(len(tipe)):
        x,y = np.random.rand(2,20)
        data.append(cs.chartDataset(x,y,tipe[i],True))
    # context["data"] = cs.chartDataset(x,y)
    return render(request,"layout/chartsSample.html",{'data': json.dumps(data)})

def choropleth(request):
    return render(request, 'layout/choropleth.html')

def bubblemap(request):
    return render(request, 'layout/bubbleMap.html')


def mapamcharts(request):
    return render(request, 'layout/mapamcharts.html')