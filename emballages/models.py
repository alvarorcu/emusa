#!/usr/bin/python
# -*- coding: utf-8 -*- 

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
LANGUAGES_CHOICES = (
    ('en', 'English'),
    ('es', 'Español'),
)

# MENU_FIELDS = {
# 	('ini', 'Inicio'),
# 	('emp', 'Empacate'),
# 	('tec', 'Tecnologia'),
# 	('gal', 'Galeria'),
# 	('cli', 'Clientes'),
# 	('con', 'Contactanos'),
# }

class data_info(models.Model):
	idioma = models.CharField(blank=True, max_length=2, choices=LANGUAGES_CHOICES, default='es')
	correo = models.EmailField(blank=True)
	telf1 = models.CharField(blank=True, max_length=250)
	telf2 = models.CharField(blank=True, max_length=250)
	telf3 = models.CharField(blank=True, max_length=250)
	logo = models.ImageField(blank=True, upload_to = 'imgs')
	menu1 = models.CharField(blank=True, max_length=20)
	menu2 = models.CharField(blank=True, max_length=20)
	menu3 = models.CharField(blank=True, max_length=20)
	menu4 = models.CharField(blank=True, max_length=20)
	menu5 = models.CharField(blank=True, max_length=20)
	menu6 = models.CharField(blank=True, max_length=20)

	def __unicode__(self):
		return self.idioma

		

class index(data_info):
	titulo_111 = models.CharField(blank=True, max_length=50)
	text_secundario111 = models.TextField(blank=True, )
	imagen111 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen112 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen113 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen114 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen115 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen116 = models.ImageField(blank=True, upload_to = 'imgs')
	
	titulo_121 = models.CharField(blank=True, max_length=50)
	text_secundario121 = models.TextField(blank=True, )
	imagen121 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen122 = models.ImageField(blank=True, upload_to = 'imgs')

	titulo_131 = models.CharField(blank=True, max_length=50)
	subtitulo131 = models.CharField(blank=True, max_length=25)
	text_secundario131 = models.TextField(blank=True, )
	subtitulo132 = models.CharField(blank=True, max_length=25)
	text_secundario132 = models.TextField(blank=True, )
	imagen131 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen132 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen133 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen134 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen135 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen136 = models.ImageField(blank=True, upload_to = 'imgs')

	titulo_141 = models.CharField(blank=True, max_length=50)
	text_secundario141 = models.TextField(blank=True, )
	imagen141 = models.ImageField(blank=True, upload_to = 'imgs')

	titulo_151 = models.CharField(blank=True, max_length=50)
	text_secundario151 = models.TextField(blank=True, )
	titulo_152 = models.CharField(blank=True, max_length=50)
	text_secundario152 = models.TextField(blank=True, )
	imagen151 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen152 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen153 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen154 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen155 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen156 = models.ImageField(blank=True, upload_to = 'imgs')
	img_certificado= models.ImageField(blank=True, upload_to = 'imgs')
	

	def __unicode__(self):
		return self.titulo_111

class emballage (data_info):
	titulo_201 = models.CharField(blank=True, max_length=50)
	text_secundario201 = models.TextField(blank=True, )
	boton_201 = models.CharField(blank=True, max_length=20)
	imagen201 = models.ImageField(blank=True, upload_to = 'imgs')

	titulo_211 = models.CharField(blank=True, max_length=50)
	text_secundario211 = models.TextField(blank=True, )
	titulo_212 = models.CharField(blank=True, max_length=50)
	text_secundario212 = models.TextField(blank=True, )
	titulo_213 = models.CharField(blank=True, max_length=50)
	text_secundario213 = models.TextField(blank=True, )
	imagen211 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen212 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen213 = models.ImageField(blank=True, upload_to = 'imgs')

	empaque_221 = models.CharField(blank=True, max_length=50)
	empaque_img221 = models.ImageField(blank=True, upload_to = 'imgs')
	empaque_222 = models.CharField(blank=True, max_length=50)
	empaque_img222 = models.ImageField(blank=True, upload_to = 'imgs')
	empaque_223 = models.CharField(blank=True, max_length=50)
	empaque_img223 = models.ImageField(blank=True, upload_to = 'imgs')
	empaque_224 = models.CharField(blank=True, max_length=50)
	empaque_img224 = models.ImageField(blank=True, upload_to = 'imgs')
	empaque_225 = models.CharField(blank=True, max_length=50)
	empaque_img225 = models.ImageField(blank=True, upload_to = 'imgs')
	empaque_226 = models.CharField(blank=True, max_length=50)
	empaque_img226 = models.ImageField(blank=True, upload_to = 'imgs')
	empaque_227 = models.CharField(blank=True, max_length=50)
	empaque_img227 = models.ImageField(blank=True, upload_to = 'imgs')
	empaque_228 = models.CharField(blank=True, max_length=50)
	empaque_img228 = models.ImageField(blank=True, upload_to = 'imgs')
	empaque_229 = models.CharField(blank=True, max_length=50)
	empaque_img229 = models.ImageField(blank=True, upload_to = 'imgs')
	empaque_220 = models.CharField(blank=True, max_length=50)
	empaque_img220 = models.ImageField(blank=True, upload_to = 'imgs')

	titulo_231 = models.CharField(blank=True, max_length=50)
	imagen231 = models.ImageField(blank=True, upload_to = 'imgs')
	titulo_232 = models.CharField(blank=True, max_length=50)
	imagen232 = models.ImageField(blank=True, upload_to = 'imgs')	
	titulo_241 = models.CharField(blank=True, max_length=50)
	imagen241 = models.ImageField(blank=True, upload_to = 'imgs')
	titulo_242 = models.CharField(blank=True, max_length=50)
	imagen242 = models.ImageField(blank=True, upload_to = 'imgs')
	titulo_243 = models.CharField(blank=True, max_length=50)
	imagen243 = models.ImageField(blank=True, upload_to = 'imgs')
	
	titulo_251 = models.CharField(blank=True, max_length=50)
	subtitulo2501 = models.CharField(blank=True, max_length=25)
	imagen2501 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2502 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2503 = models.ImageField(blank=True, upload_to = 'imgs')
	text_secundario2501 = models.TextField(blank=True, )
	subtitulo2502 = models.CharField(blank=True, max_length=25)
	imagen2504 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2505 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2506 = models.ImageField(blank=True, upload_to = 'imgs')
	text_secundario2502 = models.TextField(blank=True, )
	subtitulo2503 = models.CharField(blank=True, max_length=25)
	imagen2507 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2508 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2509 = models.ImageField(blank=True, upload_to = 'imgs')
	text_secundario2503 = models.TextField(blank=True, )
	subtitulo2504 = models.CharField(blank=True, max_length=25)
	imagen2510 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2511 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2512 = models.ImageField(blank=True, upload_to = 'imgs')
	text_secundario2504 = models.TextField(blank=True, )
	subtitulo2505 = models.CharField(blank=True, max_length=25)
	imagen2513 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2514 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2515 = models.ImageField(blank=True, upload_to = 'imgs')
	text_secundario2505 = models.TextField(blank=True, )
	subtitulo2506 = models.CharField(blank=True, max_length=25)
	imagen2516 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2517 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2518 = models.ImageField(blank=True, upload_to = 'imgs')
	text_secundario2506 = models.TextField(blank=True, )
	subtitulo2507 = models.CharField(blank=True, max_length=25)
	imagen2519 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2520 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2521 = models.ImageField(blank=True, upload_to = 'imgs')
	text_secundario2507 = models.TextField(blank=True, )
	subtitulo2508 = models.CharField(blank=True, max_length=25)
	imagen2522 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2523 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2524 = models.ImageField(blank=True, upload_to = 'imgs')
	text_secundario2508 = models.TextField(blank=True, )
	subtitulo2509 = models.CharField(blank=True, max_length=25)
	imagen2525 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2526 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2527 = models.ImageField(blank=True, upload_to = 'imgs')
	text_secundario2509 = models.TextField(blank=True, )
	subtitulo2510 = models.CharField(blank=True, max_length=25)
	imagen2528 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2529 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2530 = models.ImageField(blank=True, upload_to = 'imgs')
	text_secundario2510 = models.TextField(blank=True, )
	subtitulo2511 = models.CharField(blank=True, max_length=25)
	imagen2531 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2532 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2533 = models.ImageField(blank=True, upload_to = 'imgs')
	text_secundario2511 = models.TextField(blank=True, )
	subtitulo2512 = models.CharField(blank=True, max_length=25)
	imagen2534 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2535 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2536 = models.ImageField(blank=True, upload_to = 'imgs')
	text_secundario2512 = models.TextField(blank=True, )
	subtitulo2513 = models.CharField(blank=True, max_length=25)
	imagen2537 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2538 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2539 = models.ImageField(blank=True, upload_to = 'imgs')
	text_secundario2513 = models.TextField(blank=True, )
	subtitulo2514 = models.CharField(blank=True, max_length=25)
	imagen2540 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2541 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2542 = models.ImageField(blank=True, upload_to = 'imgs')
	text_secundario2514 = models.TextField(blank=True, )
	subtitulo2515 = models.CharField(blank=True, max_length=25)
	imagen2543 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2544 = models.ImageField(blank=True, upload_to = 'imgs')
	imagen2545 = models.ImageField(blank=True, upload_to = 'imgs')
	text_secundario2515 = models.TextField(blank=True, )
	
	boton_251 = models.CharField(blank=True, max_length=20)
	boton_252 = models.CharField(blank=True, max_length=20)
	cuestionario = models.CharField(blank=True, max_length=20)
	pregunta21 = models.CharField(blank=True, max_length=20)
	pregunta22 = models.EmailField(blank=True, ) 
	pregunta23 = models.CharField(blank=True, max_length=20)
	pregunta24 = models.CharField(blank=True, max_length=50)
	boton_253 = models.CharField(blank=True, max_length=20)

	def __unicode__(self):
		return self.titulo_201

class tecnology(data_info):
	titulo_301 = models.CharField(blank=True, max_length=50)
	text_secundario301 = models.TextField(blank=True, )
	boton_301 = models.CharField(blank=True, max_length=20)
	imagen301 = models.ImageField(blank=True, upload_to = 'imgs')

	subtitulo311 = models.CharField(blank=True, max_length=25)
	text_secundario311 = models.TextField(blank=True, )
	text_secundario312 = models.TextField(blank=True, )
	text_secundario313 = models.TextField(blank=True, )
	text_secundario314 = models.TextField(blank=True, )
	imagen311 = models.ImageField(blank=True, upload_to = 'imgs')	
	text_secundario315 = models.TextField(blank=True, )
	text_secundario316 = models.TextField(blank=True, )
	text_secundario317 = models.TextField(blank=True, )
	text_secundario318 = models.TextField(blank=True, )
	text_secundario319 = models.TextField(blank=True, )
	imagen312 = models.ImageField(blank=True, upload_to = 'imgs')

	titulo_321 = models.CharField(blank=True, max_length=50)
	imagen321 = models.ImageField(blank=True, upload_to = 'imgs')
	text_secundario321 = models.TextField(blank=True, )

	def __unicode__(self):
		return self.titulo_301

class clients(data_info):
	titulo_401 = models.CharField(blank=True, max_length=50)
	imagen401 = models.ImageField(blank=True, upload_to = 'imgs')

	def __unicode__(self):
		return self.titulo_401

class contact(data_info):
	titulo_501 = models.CharField(blank=True, max_length=50)
	pregunta51 = models.CharField(blank=True, max_length=20)
	pregunta52 = models.EmailField(blank=True, ) 
	pregunta53 = models.CharField(blank=True, max_length=20)
	pregunta54 = models.CharField(blank=True, max_length=50)
	boton_501 = models.CharField(blank=True, max_length=20)	

	def __unicode__(self):
		return self.titulo_501

class footer(data_info):
	titulo_601 = models.CharField(blank=True, max_length=50)

	def __unicode__(self):
		return self.titulo_601
