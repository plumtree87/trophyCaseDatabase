from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import RetrieveAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated,AllowAny, IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Duck
from .serializers import DuckSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class DuckList(RetrieveAPIView):

    permission_classes = []
    parser_classes = [MultiPartParser, FormParser]

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


class UsersDucks(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        usersDucks = Duck.objects.filter(user=request.user)
        serializer = DuckSerializer(usersDucks, many=True)
        return Response(serializer.data)


    def get_objectByPK(self, pk):
        try:
            return Duck.objects.get(pk=pk)
        except Duck.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        duck = self.get_objectByPK(pk)
        duck.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        duck = self.get_objectByPK(pk)
        serializer = DuckSerializer(duck, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)