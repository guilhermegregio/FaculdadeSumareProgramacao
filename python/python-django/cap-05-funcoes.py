#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cap-05-funcoes.py exemplos de utilização de função;

# Funções sem return

def funcao1():
	pass

def funcao2(parametro):
	print parametro
	
def funcao3(parametro, y="default y"):
	print parametro, y

def funcao4(parametro, y="default y", *outros):
	print parametro, y, outros
	
def funcao5(parametro, y="default y", *outros, **outros_mais):
	print parametro, y, outros, outros_mais

print "funcao1"	
funcao1()

print "funcao2"	
funcao2("primeiro")

print "funcao3"	
funcao3("primeiro")
funcao3("primeiro", "altera o default")

print "funcao4"	
funcao4("primeiro", "1",2,3,4,5,6,7,8,9,10)
funcao4("primeiro", "altera o default",1,2,3,4,5,6,7,8,9,10)

print "funcao5"	
funcao5("primeiro", "1",6,7,8,9,10,par=1, impar=0)
funcao5("primeiro", "altera o default","eita","ouro",par=1, impar=0)

#Funções com Return

def return1():
	return "teste"
	
def return2(x):
	return x
	
print return1()
print return2("Gui")
print return2(25)

