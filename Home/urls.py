from django.urls import path
from .import views

urlpatterns =   [

    path('',views.index,name='index'),
    path('SeleniumJava',views.SeleniumJava,name='SeleniumJava'),
    path('TestPage',views.TestPage,name='TestPage'),
    path('TextboxPage',views.TextboxPage,name='TextboxPage'),
    path('Introductiontoselenium',views.Introductiontoselenium,name='Introductiontoselenium'),
    path('update_server/',views.update,name='update'),
    path('Radioboxpage',views.Radioboxpage,name='Radioboxpage'),
  
]