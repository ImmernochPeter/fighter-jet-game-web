"""
Urls
"""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index-garage"),
    path(
        "add/air-to-air/",
        views.AddAirToAirRocketsView.as_view(),
        name="add-air-to-air",
    ),
]
