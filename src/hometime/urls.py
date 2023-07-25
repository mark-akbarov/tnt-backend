from django.urls import path, include

from rest_framework.routers import DefaultRouter

from hometime.views.hometime import HomeTimeRequestViewSet


router = DefaultRouter()

router.register('', HomeTimeRequestViewSet)

urlpatterns = [
    path('', include(router.urls))    
]
