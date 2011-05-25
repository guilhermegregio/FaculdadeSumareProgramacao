#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cap-05-class.py Criação de classe;
class NomeDaClasse(object):
	pass
	
class ClassePai1(object):
	def __init__(self): #Construtor
		super(ClassePai1, self).__init__()
		print "Classe pai 1"
		
class ClassePai2(object):
	def __init__(self): #Construtor
		super(ClassePai2, self).__init__()
		print "Classe pai 2"
		
class ClasseFilho(ClassePai1, ClassePai2):
	def __init__(self): #Construtor
		super(ClasseFilho, self).__init__()
		print "Classe Filho"
		
pai1 = ClassePai1()
pai2 = ClassePai2()
filho = ClasseFilho()

print type(pai1), type(pai2), type(filho)

print isinstance(pai1, ClassePai1)
print isinstance(pai2, ClassePai2)
print isinstance(filho, ClassePai1)