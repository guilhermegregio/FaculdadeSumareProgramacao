#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cap-05-metodos-instancia.py;

class Pessoa(object):
	def __init__(self, primeiro_nome, ultimo_nome):
		self.primeiro_nome = primeiro_nome
		self.ultimo_nome = ultimo_nome
	def nomeCompleto(self):
		return self.primeiro_nome + " " + self.ultimo_nome
		
pessoa = Pessoa("Terry", "Jones")

print pessoa.nomeCompleto()