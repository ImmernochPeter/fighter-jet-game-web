"""
Forms
"""

from django import forms


class AirToAirRocketForm(forms.Form):
    """
    Form for adding AirToAirRockets
    """

    max_speed = forms.FloatField(required=True)
    max_g = forms.FloatField(required=True)
    min_g = forms.FloatField(required=True)
    max_back = forms.FloatField(required=True)
    max_side = forms.FloatField(required=True)
    max_front = forms.FloatField(required=True)
    radar = forms.BooleanField(required=True)
    ir = forms.BooleanField(required=True)
