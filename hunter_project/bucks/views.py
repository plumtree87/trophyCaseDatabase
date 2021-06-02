from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Buck
from .serializers import BuckSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class BuckList(APIView):
    permission_classes = []

    def get(self, request):
        bucks = Buck.objects.all()
        serializer = BuckSerializer(bucks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BuckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsersBucks(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        usersBucks = Buck.objects.filter(user=request.user)
        serializer = BuckSerializer(usersBucks, many=True)
        return Response(serializer.data)

