# variables.tf
variable "pm_api_url" {
  description = "Proxmox API URL"
  type        = string
}
variable "pm_user" {
    description = "Proxmox user"
    type        = string
}

variable "pm_password" {
    description = "Proxmox password"
    type        = string
    sensitive   = true
}

variable "target_node" {
  description = "Proxmox target node"
  type        = string
}
variable "container_hostname" {
  description = "Hostname for the LXC container"
  type        = string
}
variable "container_root_password" {
  description = "Root password for the LXC container"
  type        = string
  sensitive   = true
}
variable "ostemplate" {
  description = "Proxmox OS template"
  type        = string
}
variable "storage" {
  description = "Proxmox storage"
  type        = string
}
variable "container_cores" {
  description = "Number of CPU cores for the container"
  type        = number
}
variable "container_memory" {
  description = "Memory allocation for the container in MB"
  type        = number
}
variable "container_swap" {
  description = "Swap allocation for the container in MB"
  type        = number
}
variable "container_disk_size" {
  description = "Disk size for the container"
  type        = string
}
variable "vm_ip" {
  description = "IP address for the VM"
  type        = string
}
variable "v_mid" {
  description = "VM ID for container"
  type        = number
  
}
variable "bridge" {
  description = "Network bridge"
  type        = string
}
variable "gateway" {
  description = "Network gateway"
  type        = string
}
variable "nameserver" {
  description = "DNS nameserver"
  type        = string
}
