from django.http import response
from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework.views import APIView

from rest_framework import status
from rest_framework.response import Response

from rest_framework import  static

from .serializers import *

class UserList(APIView):
    def get(self, request):
        model=Users.objects.all()
        serializer=UserSerializer(model,many=True)
        r=Response(serializer.data)    
        #return render(request,"apigettestpage.html",{'response': r})
        return r
    def post(self, request):
         serializer=UserSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class UserDetail(APIView):
    def get(self, request,employee_id):
        model=Users.objects.get(id=employee_id)
        serializer=UserSerializer(model)
        r=Response(serializer.data)    
        #return render(request,"apigettestpage.html",{'response': r})
        return r
    