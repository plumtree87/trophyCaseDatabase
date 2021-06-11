from django.http import Http404
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Buck
from .serializers import BuckSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, filters, generics, permissions


# Create your views here.



class BuckList(APIView):
    permission_classes = []
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        bucks = Buck.objects.all()
        serializer = BuckSerializer(bucks, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        print(request.data)
        serializer = BuckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersBucks(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        usersBucks = Buck.objects.filter(user=request.user)
        serializer = BuckSerializer(usersBucks, many=True)
        return Response(serializer.data)

    def get_objectByPK(self, pk):
        try:
            return Buck.objects.get(pk=pk)
        except Buck.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        buck = self.get_objectByPK(pk)
        buck.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        buck = self.get_objectByPK(pk)

        serializer = BuckSerializer(buck, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

