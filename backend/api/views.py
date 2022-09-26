from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class Test(APIView):
    def get(self, request, format=None):
        return Response(data={"response": True})

# Create your views here.
