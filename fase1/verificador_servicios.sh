#!/bin/bash
# Proyecto: Service Check
SERVICIO="sshd" # Probaremos con el servicio de terminal remota

if systemctl is-active --quiet $SERVICIO; then
    echo "El servicio $SERVICIO está corriendo perfectamente."
else
    echo "¡PELIGRO!: El servicio $SERVICIO está caído."
    # Aquí un DevOps real pondría: sudo systemctl start $SERVICIO
fi
