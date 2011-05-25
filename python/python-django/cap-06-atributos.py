#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cap-05-atributos.py;

class Pessoa(object):
	atributo_de_classe = "Essa eh um atributo de classe."
	def __init__(self):
		self.atributo_de_instancia = "Esse eh um atributo de instancia."
	def imprime_atributos(self):
		print Pessoa.atributo_de_classe
		print self.atributo_de_instancia
		
pessoa1 = Pessoa()
pessoa2 = Pessoa()

print Pessoa.atributo_de_classe
print pessoa1.atributo_de_classe
print pessoa2.atributo_de_classe
#Pessoa.imprime_atributos()
pessoa1.imprime_atributos()
pessoa2.imprime_atributos()

Pessoa.atributo_de_classe = "Novo valor"
print Pessoa.atributo_de_classe
print pessoa1.atributo_de_classe
print pessoa2.atributo_de_classe
#Pessoa.imprime_atributos()
pessoa1.imprime_atributos()
pessoa2.imprime_atributos()

print pessoa1.atributo_de_instancia
print pessoa2.atributo_de_instancia
#Pessoa.imprime_atributos()
pessoa1.imprime_atributos()
pessoa2.imprime_atributos()

pessoa1.atributo_de_instancia = "Novo valor para pessoa1"
print pessoa1.atributo_de_instancia
print pessoa2.atributo_de_instancia
#Pessoa.imprime_atributos()
pessoa1.imprime_atributos()
pessoa2.imprime_atributos()

#----------------------------------------------------------

class Pessoa(object):
	tabela = "cad_pessoa"
	def __init__(self):
		print "Atributos de classe:", Pessoa.tabela
		print "Atributos de instancia:", self.tabela
		
class PessoaJuridica(Pessoa):
	tabela = "cad_empresa"
	
pessoa = Pessoa()

empresa = PessoaJuridica()