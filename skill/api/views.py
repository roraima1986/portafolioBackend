from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from skill.models import Skill
from skill.api.serializers import SkillSerializer



class SkillModelViewSet(ModelViewSet):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()
    http_method_names = ['get']