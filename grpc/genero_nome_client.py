#from __future__ import print_function
#import logging

import grpc
import argparse
from pprint import pprint

import genero_nome_pb2
import genero_nome_pb2_grpc

#import genero_nome_server

def run(host, port, nome_pessoa):
	#print('run(host=%s, port=%s, nome_pessoa=%s)' % (host, port, nome_pessoa))

	channel = grpc.insecure_channel("%s:%d" % (host, port))
	#print('channel:', channel)

	stub = genero_nome_pb2_grpc.GeneroNomePreditorStub(channel)
	#stub = genero_nome_server.GeneroNomePreditor()
	#print('stub:', stub)

	request = genero_nome_pb2.GeneroNomeRequest(
		nome = nome_pessoa
	)
	#print('request:', request)

	response = stub.PreverGeneroNome(request)
	tipo = response.genero
	
	if tipo == 0:
		gen = 'FEMININO'
	elif tipo == 1:
		gen = 'MASCULINO'
	else:
		gen = ''

	print("Nome: %s => Gênero: %s" % (nome_pessoa, gen))

if __name__ == '__main__':
#	logging.basicConfig()
	parser = argparse.ArgumentParser()
	parser.add_argument('--host', help='Host do servidor', default='localhost', type=str)
	parser.add_argument('--port', help='Porta do serviço', default=50052, type=int)
	parser.add_argument('--nome', help='Nome da pessoa', default='', type=str)
	args = parser.parse_args()
	run(args.host, args.port, args.nome)

