"""
views
"""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .forms import AirToAirRocketForm
from .models import AirToAirRocket

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

    def post(self, request: HttpRequest) -> HttpResponse:
        """
        Post
        """
        form = AirToAirRocketForm(data=request.POST)
        name: str = form.data["name"]
        max_speed: float = form.data["max_speed"]
        max_g: float = form.data["max_g"]
        min_g: float = float(form.data["min_g"]) * -1
        max_back: float = form.data["max_back"]
        max_side: float = form.data["max_side"]
        max_front: float = form.data["max_front"]
        radar = False
        if "radar" in form.data:
            radar = bool(form.data["radar"])
        # pylint: disable=invalid-name
        ir = False
        if "ir" in form.data:
            ir = bool(form.data["ir"])
        # pylint: disable=no-member
        missile = AirToAirRocket.objects.create()
        missile.name = name
        missile.max_speed = max_speed
        missile.max_g = max_g
        missile.min_g = min_g
        missile.max_back = max_back
        missile.max_side = max_side
        missile.max_front = max_front
        missile.radar = radar
        missile.ir = ir
        missile.save()
        return render(request, "garage/index_garage.html")
