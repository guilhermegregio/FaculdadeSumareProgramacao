#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cap-05-closures-decorator.py;

import time

chamadas = 20

def fib(n): #calcula fibonacci de forma recursiva
	if n < 2: return 1
	return fib(n-1) + fib(n-2)
	
def memoize(fn):
	memo = {}
	def memoizer(*param1):
		key = repr(param1)
		if not key in memo:
			memo[key] = fn(*param1)
		return memo[key]
	return memoizer

t1 = time.time()
for i in range(chamadas):
	fib(i)
t2 = time.time()

# Adiciona o suporte a cache em fib
#fib = memoize(fib)
@memoize
def fib(n): #calcula fibonacci de forma recursiva
	if n < 2: return 1
	return fib(n-1) + fib(n-2)
	
t3 = time.time()
for i in range(chamadas):
	fib(i)
t4 = time.time()

print "Tempo da funcao fib() normal  (%d chamadas): %2.9fs" % (chamadas, (t2-t1))
print "Tempo da funcao fib() memoize (%d chamadas): %2.9fs" % (chamadas, (t4-t3))