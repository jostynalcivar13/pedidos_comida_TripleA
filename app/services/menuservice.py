from flask import Flask, request, jsonify, render_template
import requests
from app.models.connection import coleccion

def get_platos():
    platos = list(coleccion.menu.find())  
    for p in platos:
        p['_id'] = str(p['_id'])
    return render_template('menu.html', platos=platos)

def get_platosCurl():
    platos = list(coleccion.menu.find())  
    for p in platos:
        p['_id'] = str(p['_id'])
    return jsonify(platos)

def post_order():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    #cambiar a la ip de tu servidor de FaaS local 
    #response = requests.post("http://localhost:8000/eta", json=data)

    #cambiar a la ip de tu servidor de FaaS en docker
    response= requests.post("http://faas_app:8000/eta", json=data)

    #cambiar a tu proveedor de FaaS
    #response = requests.post("https://faas-eta.onrender.com/eta", json=data)
    
    if response.status_code != 200:
        return jsonify({"error": "No se pudo calcular ETA"}), 500

    eta = response.json().get("eta")
    data['eta'] = eta
    
    result = coleccion["orders"].insert_one(data)

    return jsonify({"message": "Pedido creado", "data": eta}), 201
