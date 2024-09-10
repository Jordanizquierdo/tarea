from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def inicio(request):
    return render(request, 'app1/index.html')

def electronica(request):
    datos= {"menu":"Electronica","p1":"mac","p2":"iPhone","p3":"Playstation","img1":"/static/img/mac.jfif","img2":"/static/img/iphone.jfif","img3":"/static/img/ps5.webp","id1":"mac","id2":"iphone","id3":"ps5"}
    return render(request, 'app1/pag.html',datos)


def juguetes(request):
    datos= {"menu":"Ropa","p1":"Auto","p2":"Pelota de Futbol","p3":"Figura de Acción","img1":"/static/img/auto.png","id1":"auto","img2":"/static/img/ball.jpg","id2":"pelota","img3":"/static/img/figura.jfif","id3":"figura"}
    return render(request, 'app1/pag.html',datos)


def ropa(request):
    datos= {"menu":"Ropa","p1":"Pantalones","p2":"Chaqueta","p3":"Camisa","img1":"/static/img/pantalones.png","id1":"pantalones","img2":"/static/img/chaqueta.png","id2":"chaqueta","img3":"/static/img/camisa.png","id3":"camisa"}
    return render(request, 'app1/pag.html',datos)