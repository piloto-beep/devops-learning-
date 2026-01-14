#!/bin/bash

# Variables elegantes
DIRECTORIO_BACKUP="Almacen_Backups"
NOMBRE_ARCHIVO="backup_total_$(date +%Y%m%d_%H%M%S).tar.gz"

echo "--- INICIANDO SISTEMA DE RESPALDO PROFESIONAL ---"

# 1. Crear el almacén si no existe
if [ ! -d "$DIRECTORIO_BACKUP" ]; then
    mkdir $DIRECTORIO_BACKUP
    echo "[+] Almacén creado."
fi

# 2. Empaquetar y Comprimir (TAR)
# Vamos a guardar todas las carpetas que creaste antes (mis_logs y mis_registros) 
# en un solo archivo comprimido.
echo "[...] Comprimiendo registros antiguos en $NOMBRE_ARCHIVO"

tar -czf $DIRECTORIO_BACKUP/$NOMBRE_ARCHIVO mis_logs/ mis_registros/ 2>/dev/null

# 3. Verificar si el comando anterior funcionó
if [ $? -eq 0 ]; then
    echo "[OK] Backup creado con éxito en $DIRECTORIO_BACKUP"
    
    # 4. Limpieza: Como ya tenemos el backup, podemos borrar las carpetas sueltas
    echo "[...] Limpiando carpetas temporales..."
    rm -rf mis_logs mis_registros
    echo "[Hecho] El sistema está limpio y respaldado."
else
    echo "[ERROR] No se pudo realizar el backup. ¿Existen las carpetas de origen?"
fi

echo "--- FIN DEL PROCESO ---"
