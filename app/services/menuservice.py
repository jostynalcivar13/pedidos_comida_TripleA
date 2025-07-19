from flask import Flask, request, jsonify, render_template
import requests
from app.models.connection import coleccion

def get_platos():
    platos = list(coleccion.menu.find())  
    for p in platos:
        p['_id'] = str(p['_id'])
    return render_template('menu.html', platos=platos)


def post_order():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    response = requests.post("https://faas-eta.onrender.com/eta", json=data)
    if response.status_code != 200:
        return jsonify({"error": "No se pudo calcular ETA"}), 500

    eta = response.json().get("eta")
    data['eta'] = eta
    
    result = coleccion["orders"].insert_one(data)


    return jsonify({"message": "Pedido creado"}), 201