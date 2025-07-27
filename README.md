# Proyecto "Comida Rápida" con Proxmox + Terraform

Este repositorio despliega una app en Docker sobre una VM de Proxmox usando Terraform.

##  Requisitos

- Proxmox VE con plantilla clonable `ubuntu-22.04-minimal-template`
- Red virtual 10.10.0.0/24 disponible (vmbr0)
- Terraform v1.0+
- SSH habilitado
- Token de acceso a Proxmox

##  Contenido

- `main.tf`: Script Terraform que:
  - Crea una VM con Ubuntu 22.04
  - Instala Docker y Docker Compose
  - Clona y ejecuta el proyecto “Comida Rápida”

##  Pasos de instalación

```bash
# 1. Clona el repositorio
git clone https://github.com/jostynalcivar13/pedidos_comida_TripleA.git

cd pedidos_comida_TripleA

# 2. Configuración del main.tf
- IP de Proxmox
- Token
- URL
- Script de instalación y ejecución del docker.

# 3. Inicializa Terraform
terraform init

# 4. Previsualiza los cambios
terraform plan

# 4. Aplica el script (crea VM y despliega app)
terraform apply ```

##  Visualización de la app
http://10.10.0.60:5000/api/platosGet
