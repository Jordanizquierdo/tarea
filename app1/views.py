from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def inicio(request):
    return render(request, 'app1/index.html')

def electronica(request):
    datos= {"menu":"Electronica","p1":"mac","p2":"iPhone","p3":"Playstation"}
    return render(request, 'app1/pag.html',datos)


def juguetes(request):
    datos= {"menu":"Ropa","p1":"Auto","p2":"Pelota de Futbol","p3":"Figura de Acción"}
    return render(request, 'app1/pag.html',datos)


def ropa(request):
    datos= {"menu":"Ropa","p1":"Pantalones","p2":"Chaqueta","p3":"Camisa"}
    return render(request, 'app1/pag.html',datos)