from django.urls import path, include

from rest_framework.routers import DefaultRouter

from tracking.views.truck import TruckIssueModelViewSet, TrailerIssueModelViewSet
from tracking.views.accident import AccidentReportViewSet


router = DefaultRouter()
router.register('trucks', TruckIssueModelViewSet)
router.register('trailers', TrailerIssueModelViewSet)
router.register('accidents', AccidentReportViewSet)

urlpatterns = [
   path('', include(router.urls)),
]

