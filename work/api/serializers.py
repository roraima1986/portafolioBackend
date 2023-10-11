from rest_framework.serializers import ModelSerializer
from work.models import Work
from skill.api.serializers import SkillSerializer


class WorkSerializer(ModelSerializer):
    skill = SkillSerializer(many=True)
    class Meta:
        model = Work
        fields = [
            'photo',
            'title',
            'skill',
            'date_project',
            'observation',
            'link_github',
            'link_website',
            'is_work',
            'is_design',
            'is_active',
        ]