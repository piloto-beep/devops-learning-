#!/bin/bash
# Proyecto: Final Pack Fase 1
echo "Preparando el paquete final de la Fase 1..."
FECHA=$(date +%Y%m%d)

# Crear un comprimido de todos tus .sh
tar -cvzf fase1_completada_$FECHA.tar.gz *.sh

echo "Paquete creado con éxito. ¡Estás listo para la Fase 2 (Python)!"
