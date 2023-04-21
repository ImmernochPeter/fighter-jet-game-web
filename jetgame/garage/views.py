"""
views
"""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import AirToAirRocketForm

# Create your views here.


class IndexView(View):
    """
    IndexView
    """

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        get
        """
        return render(request, "garage/index_garage.html")


class AddAirToAirRocketsView(View):
    """
    Add AirToAir rockets
    """

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Get
        """
        form = AirToAirRocketForm()
        return render(request, "garage/add_air_to_air.html", {"form": form})
