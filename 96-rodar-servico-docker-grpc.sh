# listar conteineres
docker ps

# remover conteiner (se existente)
docker rm $(docker ps -a -q --filter name=grpc-pessoas)

# rodar em modo interativo
#docker run --name grpc-pessoas -it grpc-pessoas

# rodar em modo daemon
docker run --name grpc-pessoas -d -p 50052:50052 grpc-pessoas
docker ps
