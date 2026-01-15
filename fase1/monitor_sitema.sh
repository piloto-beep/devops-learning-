#!/bin/bash
# Monitor de procesos pesados
echo "--- PROCESOS QUE CONSUMEN MÁS RAM ---"
ps aux --sort=-%mem | head -n 6
echo "-------------------------------------"
echo "Uso de espacio en disco actual:"
df -h | grep '^/dev/'
