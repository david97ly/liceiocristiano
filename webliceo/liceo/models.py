# coding=utf-8
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from datetime import datetime,timedelta
import time
from django.utils import timezone
import sys

class Encuesta(models.Model):
    estudiar = models.BooleanField(default=False)
    veneficiario = models.BooleanField(default=False)
    profesorado = models.BooleanField(default=False)
    comunicaciones = models.BooleanField(default=False)
    administracion = models.BooleanField(default=False)
    contaduria = models.BooleanField(default=False)
    computacion = models.BooleanField(default=False)
    juridica = models.BooleanField(default=False)
    teologia = models.BooleanField(default=False)
    nombre = models.CharField(max_length=5000,unique=True,blank=True,null=True)
    telefono = models.CharField(max_length=5000,blank=True,null=True)
    institucion_actual = models.CharField(max_length=5000,blank=True,null=True)
    comentario = models.CharField(max_length=5000,blank=True,null=True)
    

    def __str__(self):
        return str(self.nombre)