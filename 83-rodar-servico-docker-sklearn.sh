# listar conteineres
sudo docker ps

# rodar em modo interativo
#sudo docker run --name app-pessoas -it -p 80:5000 app-pessoas

# rodar em modo daemon
sudo docker run --name app-pessoas -d -p 80:5000 app-pessoas
sudo docker ps
