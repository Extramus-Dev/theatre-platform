from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import ContentCreatorSerializer, ViewerSerializer
from .models import ViewerProfile

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class SignUPViewer(APIView):
    """
    Signup viewer rest api format
    """

    def post(self, request, format=None):
        logger.debug("Viewer signup post view")
        serializer = ViewerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(f'serializer is valid: {serializer.data}')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning(f'serializer error: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignUPContentCreator(APIView):
    """
    Signup content creator rest api format
    """

    def post(self, request, format=None):
        logger.debug("Content Creator signup post view")
        serializer = ContentCreatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(f'serializer is valid: {serializer.data}')
        logger.warning(f'serializer error: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
