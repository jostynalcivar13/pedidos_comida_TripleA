# Usa una imagen oficial de Python
FROM python:3.10 
# Instala dependencias de sistema
RUN apt-get update && apt-get install -y \
    pkg-config \
    gcc \
    python3-dev \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*
# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app
# Copia los archivos del proyecto al contenedor
COPY . .
# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt
# Expone el puerto de Flask
EXPOSE 5000
# Comando para ejecutar la app Flask    
CMD ["python", "run.py", "--host=0.0.0.0", "--port=5000"]

