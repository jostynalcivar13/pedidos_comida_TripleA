from pymongo import MongoClient
from app.config import config
import os

# Detecta el entorno actual (por defecto: 'development')
env = os.getenv('FLASK_ENV', 'development')
app_config = config.get(env, config['default'])

# Obtiene la URI de MongoDB desde la configuración
mongo_uri = app_config.MONGO_URI

# Conecta con MongoDB
client = MongoClient(mongo_uri)

# Obtiene automáticamente el nombre de la base de datos desde la URI
db = client.get_database()

# definimos las colecciones
coleccion = db # o una colección específica como db['menu']


