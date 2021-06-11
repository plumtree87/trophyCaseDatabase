from django.http import Http404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import BassSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Bass


# Create your views here.


class BassList(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = []

    def get(self, request):
        fish = Bass.objects.all()
        serializer = BassSerializer(fish, many=True)
        return Response(serializer.data)

    def get_another_users_bass(self, request):
        bass = Bass.objects.filter(user=request.data)
        serializer = BassSerializer(bass, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UsersBass(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        usersBass = Bass.objects.filter(user=request.user)
        serializer = BassSerializer(usersBass, many=True)
        return Response(serializer.data)


    def get_objectByPK(self, pk):
        try:
            return Bass.objects.get(pk=pk)
        except Bass.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        bass = self.get_objectByPK(pk)
        bass.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        bass = self.get_objectByPK(pk)
        serializer = BassSerializer(bass, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)