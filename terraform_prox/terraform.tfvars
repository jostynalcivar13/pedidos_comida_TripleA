# Usa estas en su lugar:
pm_user = "root@pam"
pm_password = "tu_contraseña_aquí"
pm_api_url = "https://10.10.0.30:8006/api2/json"

# resto de tu configuración...
target_node = "pve"
container_hostname = "comidarapida"
container_root_password = "tu_contraseña_aquí"
container_cores = 2
container_memory = 1024
container_swap = 1024
container_disk_size = "20G"
v_mid = 404
ostemplate = "local:vztmpl/ct_misamisa15.tar.zst" #usa tu plantilla de Proxmox
storage = "local-lvm"
vm_ip = "10.10.0.60/24"
bridge = "vmbr0"
gateway = "10.10.0.1"
nameserver = "10.10.0.1"

