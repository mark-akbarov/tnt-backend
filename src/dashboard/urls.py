from django.urls import path

from dashboard.views.dashboard import (
    HomeTimeDashboardListView,
    TruckIssueDashboardListView,
    TrailerIssueDashboardListView,
)


urlpatterns = [
    path('hometime/', HomeTimeDashboardListView.as_view(), name='dashboard-hometime'),
    path('tracking/issues/trucks/', TruckIssueDashboardListView.as_view(), name='dashboard-truck-issue'),
    path('tracking/issues/trailers/', TruckIssueDashboardListView.as_view(), name='dashboard-trailer-issues'),
]
