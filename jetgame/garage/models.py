"""
models
"""
from django.db import models

# Create your models here.


class Weapons(models.Model):
    """
    Model for weapons
    """

    name = models.CharField(
        max_length=250, null=False, default=""
    )  # type:ignore
    weight = models.FloatField(null=False, default=0)  # type:ignore


class AirToAirRocket(Weapons):
    """
    Model for AirToAir rockets
    """

    max_speed = models.FloatField(null=False, default=0)  # type:ignore
    max_g = models.FloatField(null=False, default=0)  # type:ignore
    min_g = models.FloatField(null=False, default=0)  # type:ignore
    max_back = models.FloatField(null=False, default=0)  # type:ignore
    max_side = models.FloatField(null=False, default=0)  # type:ignore
    max_front = models.FloatField(null=False, default=0)  # type:ignore
    radar = models.BooleanField(null=False, default=False)  # type:ignore
    ir = models.BooleanField(null=False, default=False)  # type:ignore


class Enigne(models.Model):
    """
    Model for the Engine
    """

    name = models.CharField(
        max_length=250, null=False, default=""
    )  # type:ignore
    horse_power = models.FloatField(null=False, default=0)  # type:ignore
    weight = models.FloatField(null=False, default=0)  # type:ignore
    engine_count = models.IntegerField(null=False, default=0)  # type:ignore
    # consumption per minute
    consumption = models.FloatField(null=False, default=0)  # type:ignore
    afterburner = models.BooleanField(null=False, default=False)  # type:ignore
    socket = models.IntegerField(null=False, default=0)  # type:ignore


class FuelTank(models.Model):
    """
    Model for FuelTank
    """

    name = models.CharField(
        max_length=250,
        null=False,
        default="",
    )  # type:ignore
    # capacity in L
    capacity = models.FloatField(null=False, default=0)  # type:ignore
    # armor in mm
    armor = models.FloatField(null=False, default=0)  # type:ignore
    socket = models.IntegerField(null=False, default=0)  # type:ignore


class FlareModule(models.Model):
    """
    Model for FlareModule
    """

    name = models.CharField(
        max_length=250,
        null=False,
        default="",
    )  # type:ignore
    socket = models.IntegerField(null=False, default=0)  # type:ignore
    armor = models.FloatField(null=False, default=0)  # type:ignore
    ir_flare = models.IntegerField(null=False, default=0)  # type:ignore
    radar_flare = models.IntegerField(null=False, default=0)  # type:ignore


class LaserWarningSystem(models.Model):
    """
    Model for LWS
    """

    name = models.CharField(
        max_length=250, null=False, default=""
    )  # type:ignore
    socket = models.IntegerField(null=False, default=0)  # type:ignore
    armor = models.FloatField(null=False, default=0)  # type:ignore
    autoflare = models.BooleanField(null=False, default=False)  # type:ignore
    # distance in km
    distance = models.FloatField(null=False, default=0)  # type:ignore


class Jet(models.Model):
    """
    Model for Jet
    """

    name = models.CharField(
        max_length=250, null=False, default=""
    )  # type:ignore
    armor_front = models.FloatField(null=False, default=0)  # type:ignore
    armor_side = models.FloatField(null=False, default=0)  # type:ignore
    armor_back = models.FloatField(null=False, default=0)  # type:ignore
    engine_socket = models.IntegerField(null=False, default=0)  # type:ignore
    fuel_socket = models.IntegerField(null=False, default=0)  # type:ignore
    flare_socket = models.IntegerField(null=False, default=0)  # type:ignore
    lws_socket = models.IntegerField(null=False, default=0)  # type:ignore
    lws_in = models.BooleanField(null=False, default=False)  # type:ignore
    flares_in = models.BooleanField(null=False, default=False)  # type:ignore
    engine_in = models.BooleanField(null=False, default=False)  # type:ignore
    fuel_tank_in = models.BooleanField(
        null=False, default=False
    )  # type:ignore
    lws = models.ForeignKey(
        LaserWarningSystem, on_delete=models.SET_NULL, null=True
    )  # type:ignore
    flare = models.ForeignKey(
        FlareModule, on_delete=models.SET_NULL, null=True
    )  # type:ignore
    engine = models.ForeignKey(
        Enigne, on_delete=models.SET_NULL, null=True
    )  # type:ignore
