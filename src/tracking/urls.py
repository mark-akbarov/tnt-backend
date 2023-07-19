from django.urls import path, include

from rest_framework.routers import DefaultRouter

from tracking.views.truck import TruckIssueModelViewSet, TrailerIssueModelViewSet


router = DefaultRouter()
router.register('truck', TruckIssueModelViewSet)
router.register('trailer', TrailerIssueModelViewSet)

urlpatterns = [
   path('issue/', include(router.urls)),
]

