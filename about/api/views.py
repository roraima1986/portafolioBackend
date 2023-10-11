from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from about.models import About
from about.api.serializers import AboutSerializer



class AboutModelViewSet(ModelViewSet):
    serializer_class = AboutSerializer
    queryset = About.objects.all()
    http_method_names = ['get']