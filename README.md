# Proyecto "Comida Rápida" con Proxmox + Terraform

Este repositorio despliega una app en Docker sobre una VM de Proxmox usando Terraform.

---

## ✅ Requisitos

- Proxmox VE con plantilla clonable: `ubuntu-22.04-minimal-template`
- Red virtual disponible: `10.10.0.0/24` (interfaz `vmbr0`)
- Terraform v1.0 o superior
- Acceso SSH habilitado en Proxmox
- Token de acceso a Proxmox con permisos para crear VMs

---

## 📁 Contenido del repositorio

- `main.tf`: Script Terraform que:
  - Crea una VM basada en Ubuntu 22.04
  - Instala Docker y Docker Compose
  - Clona y ejecuta el proyecto “Comida Rápida”

---

## 🚀 Pasos de instalación
```bash
# 1. Clona el repositorio
git clone https://github.com/jostynalcivar13/pedidos_comida_TripleA.git

cd pedidos_comida_TripleA

# 2. Configura el archivo main.tf
# - IP del servidor Proxmox
# - Token de acceso
# - URL base de Proxmox
# - Script de instalación y despliegue de Docker

# 3. Inicializa Terraform
terraform init

# 4. Previsualiza los cambios que realizará Terraform
terraform plan

# 5. Aplica el script (crea la VM y despliega la app)
terraform apply
````

## 🌐 Visualización de la app

Una vez desplegada correctamente, puedes acceder a la API de la aplicación mediante la siguiente URL:

http://10.10.0.60:5000/api/platosGet

# API Documentation

## Tabla de Endpoints REST

| Ruta | Verbo | Descripción | Request | Response |
|------|-------|-------------|---------|----------|
| "/" | GET | Ruta raíz | | Página principal |
| "/api/platos" | GET | Obtiene el menú y lo renderiza en un plantilla html | | HTML con platos |
| "/api/platosGet" | GET | Obtiene el menú en formato json | `curl http://localhost:5000/api/platos` | `{"_id": "...", "nombre": "...", "precio": ... }]` |
| "/order" | POST | Crear una nueva orden (protegido con API Key) | `curl -X POST http://localhost:5000/order -H "Content-Type: application/json" -H "X-API-KEY: grupopatito" -d '{"items": [{"nombre":"Pizza","precio": 8.5,"cantidad":2}],"total":17.0}'` | `{"data": "2025-07-21T17:08:53.91544-05:00", "message": "Pedido creado"}` |

## Descripción de la Función FaaS

| Atributo | Detalle |
|----------|---------|
| **Nombre** | calculate_eta() |
| **Trigger** | HTTP (método POST) vía OpenFaaS gateway |
| **Lenguaje** | Python |
| **Propósito** | Recibe una lista de items y calcula el tiempo de entrega de pedido |
| **Request** | `curl -X POST http://localhost:8000/eta -H "Content-Type: application/json" -d '{"items": ["Pizza", "Coca-Cola"], "total": 18.50}'` |
| **Response** | `{"eta": "2025-07-21T17:14:10.200591-05:00"}` |


## Notas Importantes

- El endpoint `/order` requiere autenticación mediante API Key: `X-API-KEY: grupopatito`
- La función FaaS `calculate_eta()` se ejecuta a través del gateway de OpenFaaS
- Todos los timestamps siguen el formato ISO 8601 con zona horaria


