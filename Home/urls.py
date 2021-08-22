from django.urls import path
from .import views

urlpatterns =   [

    path('',views.index,name='index'),
    path('TestPage',views.TestPage,name='TestPage'),
    path('Textboxpage',views.Textboxpage,name='Textboxpage'),
    path('gettooltiptext',views.gettooltiptext,name='gettooltiptext'),
    path('Radioboxpage',views.Radioboxpage,name='Radioboxpage'),
    path('HomePage',views.HomePage,name='HomePage'),
    path('Contact',views.Contact,name='Contact'),
    path('Tooltip',views.ToolTip,name='Tooltip'),
    path('About',views.About,name='About'),
    path('SeleniumPython',views.SeleniumPython,name='SeleniumPython'),
    path('Contact',views.Contact,name='Contact'),
    path('Checkboxpage',views.Checkboxpage,name='Checkboxpage'),
    path('webdrivermanager',views.webdrivermanager,name='webdrivermanager'),
    path('alertstestpage',views.alertstestpage,name='alertstestpage'),
    path('alertshandling',views.alertshandling,name='alertshandling'),
    path('excelhandling',views.excelhandling,name='excelhandling'),
    path('introductiontoPOI',views.introductiontoPOI,name='introductiontoPOI'),
    path('readexcel',views.readexcel,name='readexcel'),
    path('writeexcel',views.writeexcel,name='writeexcel'),
    path('iframetestpage',views.iframetestpage,name='iframetestpage'),
  
]