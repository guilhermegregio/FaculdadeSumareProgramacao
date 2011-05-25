#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cap-05-seguranca.py;

ANO = 2011

class Pessoa(object):
	def __init__(self, nome, idade):
		self._nome = nome
		self._idade = idade
		self.__data_nasc = ANO - idade
		
p = Pessoa("Guilherme", 25)

print dir(p)

print p._nome #Isso nao se faz

print p._Pessoa__data_nasc #Isso se faz menos ainda