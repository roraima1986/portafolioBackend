from rest_framework.serializers import ModelSerializer
from about.models import About
from skill.api.serializers import SkillSerializer


class AboutSerializer(ModelSerializer):
    skill = SkillSerializer(many=True)
    class Meta:
        model = About
        fields = ['name', 'photo', 'description', 'skill', 'is_published']