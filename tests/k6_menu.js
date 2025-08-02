import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 50 },
    { duration: '2m', target: 50 },
  ],
};

export default function () {
  console.log('Ejecutando la prueba de carga para el menú');

  // 1. GET /platos
  let menuRes = http.get('http://localhost:5000/api/platosGet');

  check(menuRes, {
    'GET /platos status 200': (r) => r.status === 200,
  });

  // Protege el parseo con try-catch
  try {
    let menu = menuRes.json();
    console.log('Respuesta del menú:', menu);
  } catch (e) {
    console.log('Error parseando JSON de /platos:', e.message);
  }

  sleep(1);

  console.log('Realizando un pedido');

  // 2. POST /order
  let payload = JSON.stringify({
    'items': [
      {
        'nombre': "Pizza",
        'precio': 8.5,
        'cantidad': 2
      }
    ],
    'total': 17.0
  });

  let orderRes = http.post('http://localhost:5000/order', payload, {
    headers: {
      'Content-Type': 'application/json',
      'X-API-KEY': 'grupopatito'
    }
  });

  check(orderRes, {
    'POST /order status 201': (r) => r.status === 201,
  });

  try {
    console.log('Pedido realizado con éxito:', orderRes.json());
  } catch (e) {
    console.log('Error parseando JSON de /order:', e.message);
  }

  sleep(1);
}
