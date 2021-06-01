from django.shortcuts import render

# Create your views here.
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny, IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Duck
from .serializers import DuckSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class DuckList(RetrieveAPIView):

    permission_classes = []

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

