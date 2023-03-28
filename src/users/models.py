from django.db import models

# Create your models here.

class RegionModel(models.Model):
    id = models.IntegerField(primary_key=True)
    학년구분 = models.CharField(max_length=30)
    학교명 = models.CharField(max_length=30)
    학교종류 = models.CharField(max_length=30)
    nt = models.FloatField()
    nnt = models.FloatField()
    nnnt = models.FloatField()
    행정구 = models.CharField(max_length=30)

class Students(models.Model):
    id = models.IntegerField(primary_key=True)
    학년구분 = models.CharField(max_length=30)
    학교명 = models.CharField(max_length=30)
    학교종류 = models.CharField(max_length=30)
    nt = models.FloatField()
    nnt = models.FloatField()
    nnnt = models.FloatField()
    행정구 = models.CharField(max_length=30)

class Babyies(models.Model):
    id = models.IntegerField(primary_key=True)
    출생년도 = models.FloatField()
    입학년도 = models.FloatField()
    ARIMA = models.FloatField()
    SSM = models.FloatField()
    DLDA = models.FloatField()

class B(models.Model):
    id = models.IntegerField(primary_key=True)
    출생년도 = models.FloatField()
    입학년도 = models.FloatField()
    ARIMA = models.FloatField()
    SSM = models.FloatField()
    DLDA = models.FloatField()

class S(models.Model):
    id = models.IntegerField(primary_key=True)
    학년구분 = models.CharField(max_length=30)
    학교명 = models.CharField(max_length=30)
    학교종류 = models.CharField(max_length=30)
    nt = models.FloatField()
    nnt = models.FloatField()
    nnnt = models.FloatField()
    행정구 = models.CharField(max_length=30)