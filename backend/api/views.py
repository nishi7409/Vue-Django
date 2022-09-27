from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class Test(APIView):
    def get(self, request, format=None):
        return Response(data={"response": True})

class Test2(APIView):
    def post(self, request, format=None):
        number = int(request.data["val1"]) + int(request.data["val2"])
        return Response(data={"answer": number})
# Create your views here.
