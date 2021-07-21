from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request,"index.html")
def TestPage(request):
    return render(request,"TestPage.html")

def SeleniumJava(request):
    return render(request,"SeleniumJava.html")
def Introductiontoselenium(request):
    #return HttpResponse("Updated code on PythonAnywhere")
    return render(request,"introduction-to-selenium.html")
def Radioboxpage(request):
        return render(request,"Radioboxpage.html")
def HomePage(request):
        return render(request,"Home.html")
def Contact(request):
        return render(request,"Contact.html")
def ToolTip(request):
        return render(request,"Tooltip.html")
def About(request):
        return render(request,"About.html")
def SeleniumPython(request):
        return render(request,"SeleniumPython.html")
def Contact(request):
        return render(request,"Contact.html")