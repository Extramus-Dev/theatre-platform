from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import ViewerSerializer
from .models import ViewerProfile


class SignUPViewer(APIView):
    """
    Sign Up viewer Rest Api format
    """

    def post(self, request, format=None):
        serializer = ViewerSerializer(data=request.DATA)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

