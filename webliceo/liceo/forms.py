# encoding=utf-8
from django import forms
from liceo.models import *
import sys

class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        exclude = ()
        widgets = {
            'estudiar' : forms.CheckboxInput( attrs = {'id' : 'estudiar', 'name':'estudio',
            
              } ),

              'veneficiario' : forms.CheckboxInput( attrs = {'id' : 'beneficiario','name':'beneficio',
            
              } ),

              'profesorado' : forms.CheckboxInput( attrs = {'id' : 'profesorado',
            
              } ),

              'comunicaciones' : forms.CheckboxInput( attrs = {'id' : 'comunicaciones',
            
              } ),

              'administracion' : forms.CheckboxInput( attrs = {'id' : 'administracion',
            
              } ),

              'contaduria' : forms.CheckboxInput( attrs = {'id' : 'contaduria',
            
              } ),

              'computacion' : forms.CheckboxInput( attrs = {'id' : 'computacion',
            
              } ),

              'juridica' : forms.CheckboxInput( attrs = {'id' : 'juridica',
            
              } ),
              
              'teologia' : forms.CheckboxInput( attrs = {'id' : 'teologia',
            
              } ),

            'nombre' : forms.TextInput( attrs = {'id' : 'nombre',
            
              } ),

               'telefono' : forms.TextInput( attrs = {'id' : 'telefono',
            
              } ),

               'institucion_actual' : forms.TextInput( attrs = {'id' : 'institucion_actual',
            
              } ),

               'comentario' : forms.Textarea( attrs = {'id' : 'comentario','class':'com','placeholder':'Si tiene algun comentario le agradeceremos lo escriba aquí...',
            
              } ),

        


        }
