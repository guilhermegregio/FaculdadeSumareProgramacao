#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cap-05-raise.py;

class DivisaoPorZero(Exception):
	pass
	
def divisao(divisor, dividendo):
	if not dividendo: # dividendo é zero
		raise DivisaoPorZero("Divisao por zero.")
	return divisor / dividendo
	
divisao(10,0)
print divisao(10,2)