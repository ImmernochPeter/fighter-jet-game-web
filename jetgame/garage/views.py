"""
views
"""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

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
