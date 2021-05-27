
from .serializers import BassSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Bass


# Create your views here.

class BassList(APIView):

    def get(self, request):
        fish = Bass.objects.all()
        serializer = BassSerializer(fish, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
