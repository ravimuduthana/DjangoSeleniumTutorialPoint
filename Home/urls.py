from django.urls import path
from .import views

urlpatterns =   [

    path('',views.index,name='index'),
    path('SeleniumJava',views.SeleniumJava,name='SeleniumJava'),
    path('TestPage',views.TestPage,name='TestPage'),
    path('Textboxpage',views.Textboxpage,name='Textboxpage'),
    path('Introductiontoselenium',views.Introductiontoselenium,name='Introductiontoselenium'),
    path('Radioboxpage',views.Radioboxpage,name='Radioboxpage'),
    path('HomePage',views.HomePage,name='HomePage'),
    path('Contact',views.Contact,name='Contact'),
    path('Tooltip',views.ToolTip,name='Tooltip'),
    path('About',views.About,name='About'),
    path('SeleniumPython',views.SeleniumPython,name='SeleniumPython'),
    path('Contact',views.Contact,name='Contact'),
    path('Checkboxpage',views.Checkboxpage,name='Checkboxpage'),
  
]