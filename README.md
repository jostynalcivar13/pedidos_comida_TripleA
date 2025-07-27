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

---

## 🌐 Visualización de la app

Una vez desplegada correctamente, puedes acceder a la API de la aplicación mediante la siguiente URL:

```http
http://10.10.0.60:5000/api/platosGet
