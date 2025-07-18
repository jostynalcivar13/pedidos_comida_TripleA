from flask import Flask, request, jsonify, render_template

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

    result = coleccion["orders"].insert_one(data)

    return jsonify({"message": "Pedido creado", "id": str(result.inserted_id)}), 201