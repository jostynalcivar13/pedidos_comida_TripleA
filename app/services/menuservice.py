from flask import Flask, request, jsonify, render_template

from app.models.connection import coleccion



def get_platos():
    platos = list(coleccion.menu.find())  # aquí accedes a la colección "menu"
    for p in platos:
        p['_id'] = str(p['_id'])
    return render_template('menu.html', platos=platos)


def post_order():
    data = request.json
    result = mongo.db.orders.insert_one(data)
    return jsonify({"message": "Pedido creado", "id": str(result.inserted_id)}), 201
