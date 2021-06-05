from __future__ import print_function
#import logging

import grpc
import argparse

import genero_nome_pb2
import genero_nome_pb2_grpc

import genero_nome_server

def run(host, port, nome_pessoa):

	stub = genero_nome_server.GeneroNomePreditor()

	request = genero_nome_pb2.GeneroNomeRequest(
		nome = nome_pessoa
	)

	response = stub.PreverGeneroNome(request)
	print("Gênero: " + str(response.genero))

if __name__ == '__main__':
#	logging.basicConfig()
	parser = argparse.ArgumentParser()
	parser.add_argument('--host', help='Host do servidor', default='localhost', type=str)
	parser.add_argument('--port', help='Porta do serviço', default=50052, type=int)
	parser.add_argument('--nome', help='Nome da pessoa', default='', type=str)
	args = parser.parse_args()
	run(args.host, args.port, args.nome)

