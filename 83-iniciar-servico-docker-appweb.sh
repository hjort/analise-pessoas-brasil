# listar conteineres
docker ps

# remover conteiner (se existente)
docker rm $(docker ps -a -q --filter name=app-pessoas)

# rodar em modo interativo
#docker run --name app-pessoas -it -p 80:5000 app-pessoas

# rodar em modo daemon
docker run --name app-pessoas -d -p 80:5000 app-pessoas
docker ps
