from .models import Buck
from .serializers import BuckSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class BuckList(APIView):

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

