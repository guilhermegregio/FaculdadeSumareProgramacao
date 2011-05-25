#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cap-05-instancia.py;

class Pessoa(object):
	def __init__(self, parametro):
		print "Parametro", parametro
		
pessoa1 = Pessoa("Spam")

pessoa2 = Pessoa("Eggs")

print pessoa1
print pessoa2