#!/bin/bash
# Proyecto: User Audit
echo "--- USUARIOS HUMANOS EN EL SISTEMA ---"
# Filtra los usuarios que tienen una carpeta en /home
cut -d: -f1,3 /etc/passwd | egrep ":[0-9]{4}$"
echo "---------------------------------------"
echo "Usuarios con privilegios sudo:"
grep '^google\|sudo\|wheel' /etc/group
