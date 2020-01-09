from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Demo
from .serializers import DemoSerializer
import logging
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None:
        return Response({'detail': 'Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return response


class DemoView(APIView):

    def get(self, request):
        qs = Demo.objects.get(id=16)
        data = DemoSerializer(qs).data
        return  Response(data)



