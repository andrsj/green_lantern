# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class Menu(models.Model):
    menu_id = models.IntegerField(primary_key=True)
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
    restrn = models.ForeignKey('Restrn', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal'


class Restrn(models.Model):
    restrn_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    personal_id = models.IntegerField(blank=True, null=True)
    menu_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restrn'


class Restrncountry(models.Model):
    restrn = models.ForeignKey(Restrn, models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restrncountry'
        unique_together = (('restrn', 'country'),)


class Soop(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    ingrid = models.CharField(max_length=100, blank=True, null=True)
    menu = models.ForeignKey(Menu, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'soop'


class Town(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'town'
