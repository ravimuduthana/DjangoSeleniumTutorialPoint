from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
        name = {'sample_file': "gettooltiptext.html",'sample_video': "https://www.youtube.com/embed/L0I5TSDrR4A" }
        return render(request,"index.html",name)
def TestPage(request):
    return render(request,"TestPage.html")
    textboxstatus=request.POST.get("mytextbox")

def gettooltiptext(request):
    #return HttpResponse("Updated code on PythonAnywhere")
    name = {'sample_file': "gettooltiptext.html",'sample_video': "https://www.youtube.com/embed/L0I5TSDrR4A" }
    return render(request,"index.html",name)
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
def Textboxpage(request):
        return render(request,"TextboxPage.html")
def Checkboxpage(request):
        return render(request,"Checkboxpage.html")
def alertstestpage(request):
        return render(request,"alertstestpage.html")
def webdrivermanager(request):
        name = {'sample_file': "webdrivermanager.html",'sample_video': "https://www.youtube.com/embed/f4qSxXWmRIA" }
        return render(request,"index.html",name)
def alertshandling(request):
        name = {'sample_file': "alertshandling.html",'sample_video': "https://www.youtube.com/embed/6SyYCukzMG0" }
        return render(request,"index.html",name)
def excelhandling(request):
        name = {'sample_file': "introductiontoPOI.html",'sample_video': "https://www.youtube.com/embed/CbeR1c6w2U8" }
        return render(request,"excelhandling.html",name)
def introductiontoPOI(request):
        name = {'sample_file': "introductiontoPOI.html",'sample_video': "https://www.youtube.com/embed/CbeR1c6w2U8" }
        return render(request,"excelhandling.html",name)
def readexcel(request):
        name = {'sample_file': "readexcel.html",'sample_video': "https://www.youtube.com/embed/d8JZISxS0Mw" }
        return render(request,"excelhandling.html",name)
def writeexcel(request):
        name = {'sample_file': "writeexcel.html",'sample_video': "https://www.youtube.com/embed/d8JZISxS0Mw" }
        return render(request,"excelhandling.html",name)
def iframetestpage(request):
        return render(request,"iframe.html")