#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cap-05-grep2.py;

import os
import sys

class ParametroInvalido(Exception):
	pass
	
class ArquivoInvalido(Exception):
	pass
	
def busca_arquivo(str_busca, nome_arquivo):
	encontrado = False
	try:
		arquivo = open(nome_arquivo)
		for numero_linha, linha in enumerate(arquivo):
			if str_busca not in linha.strip():
				continue
			dados = (nome_arquivo, 
				numero_linha + 1, 
				linha.strip(os.linesep))
			print "%s - Linha : %s %s" % dados
			encontrado = True
		arquivo.close()
	except IOError:
		raise ArquivoInvalido("Nao consegui abrir o arquivo %s" % (nome_arquivo,))
	return encontrado

def busca(str_busca, arquivos):
	encontrado = False
	for nome_arquivo in arquivos:
		if busca_arquivo(str_busca, nome_arquivo):
			encontrado = True
	return encontrado
	return True
	
def processa_parametros(parametros):
	try:
		str_busca = parametros[0]
		lista_arquivos = parametros[1:]
	except IndexError:
		raise ParametroInvalido(u"Parametro(s) invalido(s)")
	
	if not lista_arquivos:
		raise ParametroInvalido(u"Informe o(s) arquivo(s) onde realizar a busca")
	return str_busca, lista_arquivos
	

if __name__ == "__main__":
	try:
		str_busca, lista_arquivos = processa_parametros(sys.argv[1:])
		encontrado = busca(str_busca, lista_arquivos)
		sys.exit(int(not encontrado))
	except ParametroInvalido, ex:
		print "Use: %s str lista_de_arquivos"
		print >>sys.stderr, "ERRO:",unicode(ex)
		sys.exit(-1)
	except ArquivoInvalido, ex:
		print >>sys.stderr, "ERRO:", unicode(ex)
		sys.exit(-1)