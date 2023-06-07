"""
Forms
"""

from django import forms


class AirToAirRocketForm(forms.Form):
    """
    Form for adding AirToAirRockets
    """

    name = forms.CharField(max_length=250, required=True)
    max_speed = forms.FloatField(required=True)
    max_g = forms.FloatField(required=True)
    min_g = forms.FloatField(required=True)
    max_back = forms.FloatField(required=True)
    max_side = forms.FloatField(required=True)
    max_front = forms.FloatField(required=True)
    radar = forms.BooleanField(required=True)
    ir = forms.BooleanField(required=True)
