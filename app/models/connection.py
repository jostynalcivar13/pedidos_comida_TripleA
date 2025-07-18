from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["prueba"]
coleccion = db["prb"]
        
for documento in coleccion.find():
    print("a")
    print(documento)

