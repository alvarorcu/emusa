# -*- coding: utf-8 -*- 

from django import forms
from models import index, emballage, tecnology, clients, contact, footer
from django.contrib.auth.models import User

class add_form(forms.ModelForm):

# class ModelFormOptions(object):
#    def __init__(self, options=None):
#        self.model = getattr(options, 'model', None)
#        self.fields = getattr(options, 'fields', None)
#        self.exclude = getattr(options, 'exclude', None)
#        self.widgets = getattr(options, 'widgets', None)
#        self.localized_fields = getattr(options, 'localized_fields', None)
#        self.labels = getattr(options, 'labels', None)
#        self.help_texts = getattr(options, 'help_texts', None)
#        self.error_messages = getattr(options, 'error_messages', None)
 	def __init__(self, *args, **kwargs):           
        	super(add_form, self).__init__(*args, **kwargs)
	        self.fields['titulo_111'].widget.attrs['placeholder'] = index.objects.last().titulo_111
	        self.fields['menu1'].widget.attrs['placeholder'] = index.objects.last().menu1
	        self.fields['menu2'].widget.attrs['placeholder'] = index.objects.last().menu2
	        self.fields['menu3'].widget.attrs['placeholder'] = index.objects.last().menu3
	        self.fields['menu4'].widget.attrs['placeholder'] = index.objects.last().menu4
	        self.fields['menu5'].widget.attrs['placeholder'] = index.objects.last().menu5
	        self.fields['menu6'].widget.attrs['placeholder'] = index.objects.last().menu6

	class Meta:
		model = index
		fields = '__all__'
		help_texts = {
            'menu6': '<h2>1.1 INICIO</h2>',
            'imagen116': '<h2>1.2 INICIO</h2>',
            'imagen122': '<h2>1.3 INICIO</h2>',
            'imagen136': '<h2>1.4 INICIO</h2>',
            'imagen141': '<h2>1.5 INICIO</h2>',
            'img_certificado': '<h2>2.0 EMPACATE</h2>',
        }
		labels = {
            'telf1': 'Teléfonos',
            'telf2': '',
            'telf3': '',
            'menu1': 'Menú',
            'menu2': '',
            'menu3': '',
            'menu4': '',
            'menu5': '',
            'menu6': '',
            'titulo_111': 'Texto Título',
            'text_secundario111': 'Texto Secundario',
            'imagen111': 'Empaque 1',
            'imagen112': 'Empaque 2',
            'imagen113': 'Empaque 3',
            'imagen114': 'Empaque 4',
            'imagen115': 'Empaque 5',
            'imagen116': 'Empaque 6',
            
            'titulo_121': 'Texto Título',
            'text_secundario121': 'Texto Secundario',
            'imagen121': 'Imagen 1',
            'imagen122': 'Imagen 2',

            'titulo_131': 'Texto Título',
            'subtitulo131': 'Sub Título 1',
            'text_secundario131': 'Texto Secundario 1',
            'subtitulo132': 'Sub Título 2',
            'text_secundario132': 'Texto Secundario 2',
            'imagen131': 'Imagen 1',
            'imagen132': '',
      		'imagen133': '',
            'imagen134': 'Imagen 2',
      		'imagen135': '',
            'imagen136': '',

            'titulo_141': 'Texto Título',
            'text_secundario141': 'Texto Secundario',
            'imagen141': 'INFOGRAFIA',

            'titulo_151': 'Texto Título 1',
            'text_secundario151': 'Texto Secundario 1',
            'titulo_152': 'Texto Título 2',
            'text_secundario152': 'Texto Secundario 2',
            'imagen151': 'Imagen 1',
            'imagen152': '',
            'imagen153': '',
            'imagen154': '',
            'imagen155': '',
            'imagen156': '',
            'img_certificado': 'Certificado',
        }
		widgets = {
			
			 'titulo_111' : forms.TextInput(attrs = 
				{
				'class' : 'form-control', 
				# 'placeholder' : 
				}),
			 'text_secundario111' : forms.Textarea(attrs = 
				{
				'cols' : 30,
				'rows' : 2,
				# 'size' : 100,
				'class' : 'form-control', 
				}),
			 'text_secundario121' : forms.Textarea(attrs = 
				{
				'cols' : 30,
				'rows' : 4,
				'class' : 'form-control', 
				}),
			 'text_secundario131' : forms.Textarea(attrs = 
				{
				'cols' : 45,
				'rows' : 1,
				'class' : 'form-control', 
				}),
			 'text_secundario132' : forms.Textarea(attrs = 
				{
				'cols' : 30,
				'rows' : 3,
				'class' : 'form-control', 
				}),
			 'text_secundario141' : forms.Textarea(attrs = 
				{
				'cols' : 50,
				'rows' : 2,
				'class' : 'form-control', 
				}),
			 'text_secundario151' : forms.Textarea(attrs = 
				{
				'cols' : 50,
				'rows' : 2,
				'class' : 'form-control', 
				}),
			 'text_secundario152' : forms.Textarea(attrs = 
				{
				'cols' : 50,
				'rows' : 10,
				'class' : 'form-control', 
				}),

		}

class UserRegisterForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		widgets = {
			'username' : forms.TextInput(attrs = 
				{
				'class' : 'form-control', 
				'placeholder' : 'Ingresa un nombre de usuario'
				}),
			'email' : forms.TextInput(attrs = 
				{
				'type' : 'email',
				'class' : 'form-control',
				'placeholder' : 'Ingresa un email'
				}),
			'password' : forms.TextInput(attrs = 
				{
				'type' : 'password',
				'class' : 'form-control',
				'placeholder' : 'Ingresa un password'
				})
		}

class LoginForm(forms.Form):

	username = forms.CharField(max_length=30, 
				widget = forms.TextInput(attrs = {
					'class' : 'form-control',
					'placeholder' : 'Ingresa un nombre de usuario'
					}))
	password = forms.CharField(max_length=30,
	 			widget = forms.TextInput(attrs = {
	 				'type' : 'password',
	 				'class' : 'form-control',
	 				'placeholder' : 'Ingresa un password'
	 				}))	 	 