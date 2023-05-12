from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.response import Response

# Create your views here.
class APIViewSet(viewsets.ModelViewSet):

    def retrieve(self, request):
        return Response({}, status=200)