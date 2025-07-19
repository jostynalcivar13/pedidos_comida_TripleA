import os

class Config:
    # Configuración general
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave-secreta-predeterminada')  # Valor por defecto por si no se define
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    # Configuración específica para desarrollo 
    DEBUG = True
    # Si no se define en el entorno, se conecta a localhost
    MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/pedidos")

class ProductionConfig(Config):
    # Configuración específica para producción, es decir, pa docker
    DEBUG = True
    MONGO_URI = os.environ.get("MONGO_URI", "mongodb://mongo:27017/pedidos")

# Diccionario para seleccionar configuración según el entorno
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
