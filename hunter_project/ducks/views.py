from django.shortcuts import render

# Create your views here.
from .models import Duck
from .serializers import DuckSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class DuckList(APIView):

    def get(self, request):
        ducks = Duck.objects.all()
        serializer = DuckSerializer(ducks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DuckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
