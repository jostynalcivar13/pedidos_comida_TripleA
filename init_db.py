from pymongo import MongoClient

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['pedidosya']  # poner el nombre de la base  

# tabla plato. ajustar los parametros de acuerdo a lo que queremos
platos = [
    {"id": 1, "nombre": "Hamburguesa", "precio": 3.99},
    {"id": 2, "nombre": "Pizza", "precio": 8.99},
    {"id": 3, "nombre": "Ensalada", "precio": 4.99},
    {"id": 4, "nombre": "HotDog", "precio": 2.99},
    {"id": 5, "nombre": "Tacos", "precio": 5.99},
    {"id": 6, "nombre": "Sushi", "precio": 12}
]
db.platos.insert_many(platos)

# tabla pedidos. ajustar los parametros de acuerdo a lo que queremos
pedidos = [
    {"id": 1, "plato_id": 1, "cantidad": 2, "estado": "creado", "tiempo": "10:00"},
    {"id": 2, "plato_id": 2, "cantidad": 1, "estado": "en camino", "tiempo": "10:05"},
    {"id": 3, "plato_id": 3, "cantidad": 3, "estado": "entregado", "tiempo": "20:15"},
    {"id": 4, "plato_id": 4, "cantidad": 1, "estado": "cancelado", "tiempo": "10:20"},
    {"id": 5, "plato_id": 5, "cantidad": 2, "estado": "creado", "tiempo": "30:30"},
    {"id": 6, "plato_id": 6, "cantidad": 1, "estado": "en camino", "tiempo": "10:35"},
    {"id": 7, "plato_id": 1, "cantidad": 1, "estado": "entregado", "tiempo": "30:40"},
    {"id": 8, "plato_id": 2, "cantidad": 2, "estado": "cancelado",  "tiempo": "10:45"},
    {"id": 9, "plato_id": 3, "cantidad": 1, "estado": "creado", "tiempo": "15:50"},
    {"id": 10, "plato_id": 4, "cantidad": 3, "estado": "en camino", "tiempo": "30:55"},
]
db.pedidos.insert_many(pedidos)

# tabla usuarios. ajustar los parametros de acuerdo a lo que queremos
usuarios = [
    {"id": 1, "nombre": "Juan", "email": "juan@gmail.com"},
    {"id": 2, "nombre": "Maria", "email": "maria@gmail.com"},
    {"id": 3, "nombre": "Pedro", "email": "pedro@gmail.com"},
    {"id": 4, "nombre": "Ana", "email": ""},
    {"id": 5, "nombre": "Luis", "email": ""},
    {"id": 6, "nombre": "Laura", "email": ""}
]
db.usuarios.insert_many(usuarios)
    

print("Datos iniciales insertados a la base.")
