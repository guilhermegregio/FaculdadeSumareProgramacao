#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cap-05-propriedades.py;

class Forno(object):
	def __init__(self):
		self._temperatura = 0
		
	def _get_temperatura(self):
		print "Temperatura atual:", self._temperatura
		return self._temperatura
	def _set_temperatura(self, temperatura):
		if temperatura > 250:
			raise ValueError("Temperatura maxima do forno: 250")
		self._temperatura = temperatura
		print "Nova temperatura:", temperatura
	temperatura = property(_get_temperatura, _set_temperatura)
	
forno = Forno()

forno.temperatura

forno.temperatura = 120

forno.temperatura

forno.temperatura = 300