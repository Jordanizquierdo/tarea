from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def inicio(request):
    return render(request, 'app1/index.html')

def electronica(request):
    datos= {"menu":"Electronica","p1":"mac","p2":"iPhone","p3":"Playstation"}
    return render(request, 'app1/pag.html',datos)