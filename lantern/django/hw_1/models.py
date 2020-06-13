# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    start = models.DateField(blank=True, null=True)
    finish = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class Personal(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    posada = models.CharField(max_length=30, blank=True, null=True)
    restaurant = models.ForeignKey('Restaurant', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal'


class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    counrtry_id = models.IntegerField(blank=True, null=True)
    personal_id = models.IntegerField(blank=True, null=True)
    menu_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurant'


class Restaurantcountry(models.Model):
    restaurant = models.ForeignKey(Restaurant, models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurantcountry'
        unique_together = (('restaurant', 'country'),)


class Restaurantmenu(models.Model):
    restaurant = models.ForeignKey(Restaurant, models.DO_NOTHING, blank=True, null=True)
    menu = models.ForeignKey(Menu, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurantmenu'
        unique_together = (('restaurant', 'menu'),)


class Soop(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    ingredient = models.CharField(max_length=100, blank=True, null=True)
    menu = models.ForeignKey(Menu, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'soop'


class Town(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    counrty = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'town'
