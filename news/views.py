from sitesupernova.settings import STATIC_ROOT, STATIC_URL
from django.http import HttpResponse
from django.shortcuts import render
from .models import News


def news(request):
    n=News.objects.all()
    c=News.objects.filter(carrossel=True)
    print(c)
    print(n)
    return render(request,"news/news.html", {"news":n, "carrossel":c}) 

def programacao(request):
    n=News.objects.all()
#    print(n)
    return render(request,"news/programacao.html", {"news":n})

def noticias(request):
    n=News.objects.all()
#   print(n)
    return render(request,"news/noticias.html", {"news":n})

def contato(request):
    n=News.objects.all()
#    print(n)
    return render(request,"news/contato.html", {"news":n})

def noticia1(request):
    n=News.objects.all()
#    print(n)
    return render(request,"news/noticias/noticia1.html", {"news":n})