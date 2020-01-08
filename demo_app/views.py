from rest_framework import generics
from .models import Demo
from .serializers import DemoSerializer


class DemoView(generics.ListCreateAPIView):
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer

