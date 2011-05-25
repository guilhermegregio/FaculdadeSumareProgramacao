#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cap-05-yield.py yield generators;

db = (
	((2009, 01, 05), "rec1"),
	((2009, 02, 05), "rec2"),
	((2009, 03, 05), "rec3"),
	((2009, 04, 05), "rec4"),
	((2009, 05, 05), "rec5"),
	((2009, 06, 05), "rec6"),
)

def busca(dt_ini, dt_fim):
	for rec in db:
		if rec[0] >= dt_ini and rec[0] <= dt_fim:
			msg = yield rec[1]
			if msg:
				print rec[1], msg

for row in busca((2009,03,01), (2009,05,01)):
	print row

b = busca((2009,03,01), (2009,05,01))
print b.next()
b.send("OK")

try:
	print b.next()
except StopIteration:
	pass
	
def countfrom(n):
    while True:
        yield n
        n += 1

for i in countfrom(10):
    if i <= 20:
        print i
    else:
        break