from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["pedidos"]  # nombre de tu base de datos
coleccion = db 
