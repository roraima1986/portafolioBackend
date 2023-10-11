from rest_framework.routers import DefaultRouter
from work.api.views import WorkModelViewSet

router_work = DefaultRouter()

router_work.register(prefix='work', basename='work', viewset=WorkModelViewSet)