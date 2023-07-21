from django.urls import path, include

from rest_framework.routers import DefaultRouter

from tracking.views.truck import TruckIssueModelViewSet, TrailerIssueModelViewSet


router = DefaultRouter()
router.register('trucks', TruckIssueModelViewSet)
router.register('trailers', TrailerIssueModelViewSet)

urlpatterns = [
   path('issues/', include(router.urls)),
]

