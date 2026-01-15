#!/bin/bash
# Proyecto: Alerta de Recursos
echo "--- VERIFICANDO SALUD DEL SISTEMA ---"

# Obtiene el uso de CPU (redondeado)
CPU_LOAD=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
MEM_FREE=$(free | grep Mem | awk '{print $4/$2 * 100.0}')

echo "Uso de CPU: $CPU_LOAD%"
echo "Memoria Libre: $MEM_FREE%"

# Si el CPU es mayor a 80 (puedes cambiarlo para probar)
if (( $(echo "$CPU_LOAD > 80" | bc -l) )); then
    echo "¡ALERTA!: El uso de CPU es crítico."
fi
