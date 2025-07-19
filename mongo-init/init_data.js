db = db.getSiblingDB('pedidos'); 

db.menu.insertMany([
  {
    "nombre": "Hamburguesa Doble",
    "descripcion": "Deliciosa hamburguesa con doble carne, queso cheddar y vegetales frescos.",
    "precio": 6.99,
    "imagen": "hamburguesa.jpg",
    "disponible": "true"
  },
  {
    "nombre": "Pizza Personal",
    "descripcion": "Pizza individual con salsa de tomate, queso mozzarella y pepperoni.",
    "precio": 5.50,
    "imagen": "pizza.jpg",
    "disponible": "true"
  },
  {
    "nombre": "Ensalada César",
    "descripcion": "Lechuga fresca, pollo a la plancha, crutones y aderezo César.",
    "precio": 4.25,
    "imagen": "ensalada.jpg",
    "disponible": "true"
  },
  {
    "nombre": "Papas Fritas",
    "descripcion": "Porción de papas fritas crujientes.",
    "precio": 2.50,
    "imagen": "papas.jpg",
    "disponible": "true"
  },
  {
    "nombre": "Refresco Grande",
    "descripcion": "Bebida gaseosa de 500ml a elección.",
    "precio": 1.50,
    "imagen": "refresco.jpg",
    "disponible": "true"
  }
]);

print("✅ Datos iniciales insertados en 'pedidos.menu'");
