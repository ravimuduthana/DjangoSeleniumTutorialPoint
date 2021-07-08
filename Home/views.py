from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def index(request):
    return render(request,"index.html")
def TestPage(request):
    return render(request,"TestPage.html")
def TextboxPage(request):
    return render(request,"TextboxPage.html")
def SeleniumJava(request):
    return render(request,"SeleniumJava.html")
def Introductiontoselenium(request):
    return render(request,"introduction-to-selenium.html")