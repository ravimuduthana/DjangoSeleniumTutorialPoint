from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import git
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
    #return HttpResponse("Updated code on PythonAnywhere")
    return render(request,"introduction-to-selenium.html")
@csrf_exempt
def update(request):
     if request.method == "POST":
        '''
        pass the path of the diectory where your project will be 
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
        '''
        repo = git.Repo("ravimuduthana.pythonanywhere.com/") 
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere")
     else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")
def Radioboxpage(request):
        return render(request,"Radioboxpage.html")