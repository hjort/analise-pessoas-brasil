from platform import python_version
print('Python Versão:', python_version())

import grpc
import time
import joblib
from os import path
from concurrent import futures
from pprint import pprint
import re
import numpy as np

import genero_nome_pb2
import genero_nome_pb2_grpc

# número de segundos por dia
ONE_DAY_IN_SECONDS = 60 * 60 * 24

# modelo preditivo previamente treinado
MODELO_TREINADO = '../modelos/modelo-genero-nome.joblib.bz2'

MAIOR_QTDE_LETRAS = 16

class GeneroNomePreditor(genero_nome_pb2_grpc.GeneroNomePreditorServicer):
	_modelo = None

	@classmethod
	def obter_modelo(cls):
		print('obter_modelo()')
		pprint(cls._modelo)
		if cls._modelo is None:
			caminho = path.join(path.dirname(path.abspath(__file__)), MODELO_TREINADO)
			print("caminho:", caminho)
			cls._modelo = joblib.load(caminho)
		return cls._modelo

	def PreverGeneroNome(self, request):
		print('PreverGeneroNome()')
		modelo = self.__class__.obter_modelo()

		#pprint(self)
		#pprint(request)
		#print(type(request))
		#pprint(request.nome)
		nome_pessoa = request.nome
		print('=> nome:', nome_pessoa)

		# extrair primeiro nome e obter array de letras invertido
		anome = self.obter_array_letras(self.obter_primeiro_nome(nome_pessoa))

		# prever o gênero a partir do nome
		if anome:
			tipo = modelo.predict(np.asarray([anome]))[0]
		else:
			tipo = None

		'''if tipo == 0:
			gen = 'FEMININO'
		elif tipo == 1:
			gen = 'MASCULINO'
		else:
			gen = ''
		print(' > genero:', gen)'''

		return genero_nome_pb2.GeneroNomeReply(genero=tipo)

	def obter_primeiro_nome(self, str):
		if str:
			return re.split("\s", str)[0].upper()

	def obter_array_letras(self, str):
		if not str:
			return None
		rev = str[::-1]
		anome = []
		for i in range(MAIOR_QTDE_LETRAS):
			x = ord(rev[i]) - 64 if len(rev) > i else 0
			anome.append(x)
		return anome


def serve():
	print('serve()')
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	genero_nome_pb2_grpc.add_GeneroNomePreditorServicer_to_server(GeneroNomePreditor(), server)
	server.add_insecure_port('[::]:50052')
	server.start()
	try:
		while True:
			time.sleep(ONE_DAY_IN_SECONDS)
	except KeyboardInterrupt:
		server.stop(0)

if __name__ == '__main__':
	serve()

