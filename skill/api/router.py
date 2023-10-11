from rest_framework.routers import DefaultRouter
from skill.api.views import SkillModelViewSet

router_skill = DefaultRouter()

router_skill.register(prefix='skill', basename='skill', viewset=SkillModelViewSet)