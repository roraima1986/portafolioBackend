from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from work.models import Work
from work.api.serializers import WorkSerializer



class WorkModelViewSet(ModelViewSet):
    serializer_class = WorkSerializer
    queryset = Work.objects.all()
    http_method_names = ['get']