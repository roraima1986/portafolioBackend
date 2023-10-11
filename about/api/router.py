from rest_framework.routers import DefaultRouter
from about.api.views import AboutModelViewSet

router_about = DefaultRouter()

router_about.register(prefix='about', basename='about', viewset=AboutModelViewSet)