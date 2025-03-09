from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .serializers import BookSerializer

from .models import Book


@api_view(['GET'])
def BookList(request) :
   if request.method == "GET":
      seriaizer  = BookSerializer(data = request.data)
      if seriaizer.is_valid():
         seriaizer.save()
         return Response(seriaizer.data, status.HTTP_200_OK)
   return Response(seriaizer.data, status.HTTP_400_BAD_REQUEST)  
