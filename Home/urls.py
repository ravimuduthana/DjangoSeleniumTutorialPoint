from django.urls import path
from .import views

urlpatterns =   [

    path('',views.index,name='index'),
    path('SeleniumJava',views.SeleniumJava,name='SeleniumJava'),
    path('TestPage',views.TestPage,name='TestPage'),
    path('TextboxPage',views.TextboxPage,name='TextboxPage'),
    path('Introductiontoselenium',views.Introductiontoselenium,name='Introductiontoselenium'),
    path('Radioboxpage',views.Radioboxpage,name='Radioboxpage'),
    path('HomePage',views.HomePage,name='HomePage'),
    path('Contact',views.Contact,name='Contact'),
    path('ToolTip',views.ToolTip,name='ToolTip'),
    path('About',views.About,name='About'),
    path('SeleniumPython',views.SeleniumPython,name='SeleniumPython'),
  
]