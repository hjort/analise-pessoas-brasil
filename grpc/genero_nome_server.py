import grpc
import time
import joblib
from os import path
from concurrent import futures
from pprint import pprint

import genero_nome_pb2
import genero_nome_pb2_grpc

# número de segundos por dia
ONE_DAY_IN_SECONDS = 60 * 60 * 24

# modelo preditivo previamente treinado
MODELO_TREINADO = '../modelos/modelo-genero-nome.joblib.bz2'

class GeneroNomePreditor(genero_nome_pb2_grpc.GeneroNomePreditorServicer):
	_modelo = None

	@classmethod
	def obter_modelo(cls):
		print('obter_modelo()')
		if cls._modelo is None:
			caminho = path.join(path.dirname(path.abspath(__file__)), MODELO_TREINADO)
			print("caminho:", caminho)
			cls._modelo = joblib.load(caminho)
		return cls._modelo

	def PreverGeneroNome(self, request):
		print('PreverGeneroNome()')
		modelo = self.__class__.obter_modelo()
		nome_pessoa = request.nome
		print('=> nome:', nome)
		res = modelo.predict([[nome_pessoa]])
		print(' > genero:', res)
		return genero_nome_pb2.GeneroNomeReply(genero=res[0])

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

