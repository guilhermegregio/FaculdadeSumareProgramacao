#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cap-05-try.py;

def le_arquivo(arquivo):
	try:
		arq = open(arquivo)
		try:
			linha1 = arq.readline()
			linha2 = arq.readline()
		finally:
			print "Erro ao ler conteudo. Fechando arquivo"
			arq.close()
	except Exception, e:
		print "Erro ao abrir o arquivo. O erro ocorrido foi: "
		print str(e)
		
le_arquivo("nao_existe.txt")