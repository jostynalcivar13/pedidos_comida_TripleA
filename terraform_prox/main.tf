    terraform {
        required_providers {
            proxmox = {
                source  = "Telmate/proxmox"
                version = "~> 2.9.0"
            }
        }
    }

    provider "proxmox" {
        pm_api_url      = var.pm_api_url
        pm_user         = var.pm_user
        pm_password     = var.pm_password
        pm_tls_insecure = true
    }

    resource "proxmox_lxc" "docker_container" {
        vmid         = var.v_mid
        hostname     = var.container_hostname
        ostemplate   = var.ostemplate
        target_node  = var.target_node
        unprivileged = false
        onboot       = true
        cores        = var.container_cores
        memory       = var.container_memory
        swap         = var.container_swap
        password     = var.container_root_password

        # Opciones adicionales para contenedor privilegiado
        tags = "docker"

        rootfs {
            storage = var.storage
            size    = var.container_disk_size
        }

        network {
            name   = "eth0"
            bridge = var.bridge
            ip     = var.vm_ip
            gw     = var.gateway
        }

        nameserver = var.nameserver
        start = true

        provisioner "file" {
            source      = "install.sh"
            destination = "/tmp/install.sh"
            
            connection {
                type     = "ssh"
                host     = split("/", var.vm_ip)[0]
                user     = "root"
                password = var.container_root_password
                timeout  = "40m"
            }
        }

        provisioner "remote-exec" {
            connection {
                type     = "ssh"
                host     = split("/", var.vm_ip)[0]
                user     = "root"
                password = var.container_root_password
                timeout  = "40m"
            }
            
            inline = [
                "chmod +x /tmp/install.sh",
                "/tmp/install.sh"
            ]
        }
    }