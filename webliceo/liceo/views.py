# coding=utf-8
from django.shortcuts import render, get_object_or_404,redirect,get_list_or_404,render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import get_template
from django.template import Context
from django.template.context import RequestContext
from django.core import serializers
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import *
from django.views.generic import TemplateView, FormView,CreateView, UpdateView
#from django.core.urlresolvers import reverse_lazy, reverse
from .models import *
from random import choice
#from liceo.metodos import *
from decimal import Decimal
from datetime import datetime,timedelta
import time
import hashlib
from django.utils import timezone
import pytz
from django.core.mail import EmailMessage
from django.db.models import Q
#from .htmltopdf import render_to_pdf
from datetime import *
from django.template.defaultfilters import slugify
import sys



def home(request):
    template = "index.html"

    titulo ="Liceo Cristiano Cara Sucia"
    context = {"titulo":titulo}
    return render(request,template,context)

class RegistrarEncuesta(CreateView):

    form_class = EncuestaForm
    template_name = "encuesta.html"
    success_url = '/'

    def form_valid(self,form):
        form.save()
        return super(RegistrarEncuesta,self).form_valid(form)


@login_required(login_url='/')
def graficos(request):
    computacion = Encuesta.objects.filter(computacion=True).count()
    contaduria = Encuesta.objects.filter(contaduria=True).count()
    administracion = Encuesta.objects.filter(administracion=True).count()
    comunicaciones = Encuesta.objects.filter(comunicaciones=True).count()
    profesorado = Encuesta.objects.filter(profesorado=True).count()
    teologia = Encuesta.objects.filter(teologia=True).count()
    juridica = Encuesta.objects.filter(juridica=True).count()

    total = Decimal(computacion+contaduria+administracion+comunicaciones+profesorado+teologia+juridica)
    
    porcomputacion = Decimal((computacion*100)/total)
    porcontaduria = Decimal((contaduria*100)/total)
    poradministracion = Decimal((administracion*100)/total)
    porcomunicaciones = Decimal((comunicaciones*100)/total)
    porprofesorado = Decimal((profesorado*100)/total)
    porteologia = Decimal((teologia*100)/total)
    porjuridica = Decimal((juridica*100)/total)


    portotal = Decimal(porcomputacion+porcontaduria+poradministracion+porcomunicaciones+porprofesorado+porteologia+porjuridica)
    
    class Dato():
       carrera = ""
       cantidad = 0
       porcentaje = 0

    listadatos =[]

    dat = Dato()
    dat.carrera = "Ingenieria"
    dat.cantidad = computacion
    dat.porcentaje = porcomputacion

    listadatos.append(dat)

    dat = Dato()
    dat.carrera = "Contaduria"
    dat.cantidad = contaduria
    dat.porcentaje = porcontaduria

    listadatos.append(dat)
    dat = Dato()
    dat.carrera = "Administracion"
    dat.cantidad = administracion
    dat.porcentaje = poradministracion

    listadatos.append(dat)
    dat = Dato()
    dat.carrera = "Comunicaciones"
    dat.cantidad = comunicaciones
    dat.porcentaje = porcomunicaciones

    listadatos.append(dat)
    dat = Dato()
    dat.carrera = "Educacion"
    dat.cantidad = profesorado
    dat.porcentaje = porprofesorado

    listadatos.append(dat)
    dat = Dato()
    dat.carrera = "Teologia"
    dat.cantidad = teologia
    dat.porcentaje = porteologia

    listadatos.append(dat)
    dat = Dato()
    dat.carrera = "Juridica"
    dat.cantidad = juridica
    dat.porcentaje = porjuridica

    listadatos.append(dat)
    

    for i in listadatos:
        print(i.cantidad)

   

    context = {'lista': listadatos,'total':total,'portotal':portotal}
  

    template ="graficos.html"
   

    return render(request,template,context)