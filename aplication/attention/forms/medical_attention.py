from django.forms import ModelForm, ValidationError
from django import forms

from aplication.attention.models import Atencion
from aplication.core.models import Paciente

# Definición de la clase PatientForm que hereda de ModelForm
class AttentionForm(ModelForm):
        # Clase interna Meta para configurar el formulario
    class Meta:    
        # campos que se muestran en este mismo orden en el formulario como etiquetas html
        # fields = [  "paciente",
        #             "fecha_atencion",
        #             "presion_arterial",
        #             "pulso",
        #             "temperatura",
        #             "frecuencia_respiratoria",
        #             "saturacion_oxigeno",
        #             "peso",
        #             "altura",
        #             "motivo_consulta",
        #             "sintomas",
        #             "tratamiento",
        #             "diagnostico",
        #             "examen_fisico",
        #             "examenes_enviados",
        #             "comentario_adicional"
        #          ]
        model = Atencion
        fields = '__all__'
        exclude = ['fecha_atencion']  # Se excluye porque es auto_now_add
        
        widgets = {
            'paciente': forms.Select(attrs={
                'class': 'form-select shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'id': 'id_paciente',
            }),
            'presion_arterial': forms.TextInput(attrs={
                'class': 'form-control shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': 'Ej: 120/80',
                'id': 'id_presion_arterial',
            }),
            'pulso': forms.NumberInput(attrs={
                'class': 'form-control shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': 'Ingrese el pulso en ppm',
                'id': 'id_pulso',
            }),
            'temperatura': forms.NumberInput(attrs={
                'class': 'form-control shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': 'Ingrese la temperatura en °C',
                'step': '0.1',
                'id': 'id_temperatura',
            }),
            'frecuencia_respiratoria': forms.NumberInput(attrs={
                'class': 'form-control shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': 'Ingrese la frecuencia respiratoria en rpm',
                'id': 'id_frecuencia_respiratoria',
            }),
            'saturacion_oxigeno': forms.NumberInput(attrs={
                'class': 'form-control shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': 'Ingrese la saturación de oxígeno en %',
                'step': '0.01',
                'id': 'id_saturacion_oxigeno',
            }),
            'peso': forms.NumberInput(attrs={
                'class': 'form-control shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': 'Ingrese el peso en kg',
                'step': '0.01',
                'id': 'id_peso',
            }),
            'altura': forms.NumberInput(attrs={
                'class': 'form-control shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': 'Ingrese la altura en m',
                'step': '0.01',
                'id': 'id_altura',
            }),
            'motivo_consulta': forms.Textarea(attrs={
                'class': 'form-control shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': 'Describa el motivo de la consulta',
                'rows': 4,
                'id': 'id_motivo_consulta',
            }),
            'sintomas': forms.Textarea(attrs={
                'class': 'form-control shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': 'Describa los síntomas',
                'rows': 4,
                'id': 'id_sintomas',
            }),
            'tratamiento': forms.Textarea(attrs={
                'class': 'form-control shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': 'Describa el plan de tratamiento',
                'rows': 4,
                'id': 'id_tratamiento',
            }),
            'diagnostico': forms.SelectMultiple(attrs={
                'class': 'form-select multiple shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'id': 'id_diagnostico',
            }),
            'examen_fisico': forms.Textarea(attrs={
                'class': 'form-control shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': 'Describa el examen físico realizado',
                'rows': 4,
                'id': 'id_examen_fisico',
            }),
            'examenes_enviados': forms.Textarea(attrs={
                'class': 'form-control shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': 'Liste los exámenes enviados',
                'rows': 4,
                'id': 'id_examenes_enviados',
            }),
            'comentario_adicional': forms.Textarea(attrs={
                'class': 'form-control shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': 'Comentarios adicionales',
                'rows': 4,
                'id': 'id_comentario_adicional',
            }),
        } 
        labels={
          "saturacion_oxigeno":"saturacion_oxigeno",
          "frecuencia_respiratoria":"frecuencia_respiratoria",
            
        }
      
     
       
      
