#!/bin/bash

sudo apt-get update -y 
sudo apt-get install -y docker.io docker-compose git ufw
sudo systemctl start docker
sudo systemctl enable docker

sudo mkdir -p /home/comida-rapida

# Clonamos el proyecto
sudo git clone https://github.com/jostynalcivar13/pedidos_comida_TripleA.git /home/comida-rapida

cd /home/comida-rapida/

# Esperar a que Docker esté listo
sleep 10

#abre los puertos para la app y la faas
sudo ufw allow 5000/tcp
sudo ufw allow 8000/tcp

# Ejecuta docker-compose
sudo docker-compose up -d --build

echo "Instalación completada con éxito"