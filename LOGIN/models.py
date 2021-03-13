from django.db import models


# Create your models here.
class QCWYInfo(models.Model):
    url = models.CharField(max_length=255)
    keywd = models.CharField(max_length=255)


class WtKeyWd(models.Model):
    url = models.CharField(max_length=255)
    keywd = models.CharField(max_length=255)


class RtKeyWd(models.Model):
    url = models.CharField(max_length=255)
    keywd = models.CharField(max_length=255)


class EdKeyWd(models.Model):
    url = models.CharField(max_length=255)
    keywd = models.CharField(max_length=255)


class CnKeyWd(models.Model):
    url = models.CharField(max_length=255)
    keywd = models.CharField(max_length=255)


class XcKeyWd(models.Model):
    url = models.CharField(max_length=255)
    keywd = models.CharField(max_length=255)


class WeKeyWd(models.Model):
    url = models.CharField(max_length=255)
    keywd = models.CharField(max_length=255)


class HyKeyWd(models.Model):
    url = models.CharField(max_length=255)
    keywd = models.CharField(max_length=255)


class CsKeyWd(models.Model):
    url = models.CharField(max_length=255)
    keywd = models.CharField(max_length=255)


class Location(models.Model):
    url = models.CharField(max_length=255)
    keywd = models.CharField(max_length=255)


class ZyKeyWd(models.Model):
    url = models.CharField(max_length=255)
    keywd = models.CharField(max_length=255)

