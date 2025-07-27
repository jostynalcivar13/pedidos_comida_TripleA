from pymongo import MongoClient

#cambiar a localhost si se usa en local
#client = MongoClient("mongodb://localhost:27017/")

#cambiar a mongo si se usa en docker
client = MongoClient("mongodb://mongo:27017/")
 
db = client["pedidos"]  
coleccion = db 