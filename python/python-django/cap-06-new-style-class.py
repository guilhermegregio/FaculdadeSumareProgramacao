#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cap-05-new-style-class.py Criação de classe;

class Pessoa(object):
	def __init__(self, nome):
		self.nome = nome
		
class PessoaJuridica(Pessoa):
	def __init__(self, nome):
		super(PessoaJuridica, self).__init__(nome)
		self.cnpj = "" # empresas tem CNPJ
		
class PessoaFisica(Pessoa):
	def __init__(self, nome):
		super(PessoaFisica, self).__init__(nome)
		self.cpf = "" # pessoas tem cpf
		
pessoa1 = Pessoa("Guilherme")
pessoa2 = PessoaJuridica("Marcia")
pessoa3 = PessoaFisica("Viviane")

print issubclass(PessoaJuridica, Pessoa)
print issubclass(PessoaFisica, Pessoa)
print issubclass(Pessoa, PessoaJuridica)

print isinstance(pessoa1, Pessoa)
print isinstance(pessoa1, PessoaJuridica)
print isinstance(pessoa2, Pessoa)
print isinstance(pessoa2, PessoaJuridica)
print isinstance(pessoa3, Pessoa)
print isinstance(pessoa3, PessoaJuridica)
print isinstance(pessoa3, PessoaFisica)
