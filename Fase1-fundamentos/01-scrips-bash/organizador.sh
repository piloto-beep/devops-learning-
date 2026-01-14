# 1. Definir variables (las cajitas de informacion)

USUARIO=$(whoami)
FECHA=$(date +%Y-%m-%d)

echo "___ Iniciacionado Limpieza para el usuario: $USUARIO ___"

2. Crear carpetas de organizaion si no existen

mkdir -p Documentos_Importantes Reportes_Sistema

# 3 Crear un archivo de reporte con informacion del sistema 

echo "Reporte generado el: $FECHA" > Reportes_Sistema/estado_disco.txt
echo "--------------------------" >> Reportes_Sitema/estadp_disco.txt
df -h | grep '^/dev/' >> Reportes_Sistema/estado_disco.txt
# 4. Mover cualquier archivo .txt que esté suelto a la carpeta de reportes
# (Esto es automatización real: mover cosas por nosotros)
mv *.txt Reportes_Sistema/ 2>/dev/null

echo "Limpieza completada. Se ha generado un reporte en la carpeta Reportes_Sistema."
ls -R

