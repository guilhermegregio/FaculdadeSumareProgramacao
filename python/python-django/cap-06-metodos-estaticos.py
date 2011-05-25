#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cap-05-metodos-estaticos.py;

class Pessoa(object):
	def __init__(self, tipo="fisica"):
		print "Pessoa", tipo
	@staticmethod
	def cria_pessoa_juridica():
		return Pessoa("juridica")
		
	@staticmethod
	def cria_pessoa_fisica():
		return Pessoa()

print Pessoa.cria_pessoa_fisica()
print Pessoa.cria_pessoa_juridica()
