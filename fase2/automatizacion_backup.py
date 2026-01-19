import shutil
import datetime
import os

def crear_backup():
    # 1. Definimos origen y destino
    origen = "datos_proyectos"
    destino_carpeta = "backups"
    
    # 2. Generamos un nombre único con la fecha y hora actual
    # Ejemplo: backup_2026-01-19_12-30-00
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_archivo = f"backup_{timestamp}"
    
    # Ruta completa final (ej: backups/backup_2026...)
    ruta_final = os.path.join(destino_carpeta, nombre_archivo)
    
    print(f"📦 Iniciando copia de seguridad de '{origen}'...")
    
    try:
        # 3. Creamos el archivo ZIP comprimido
        shutil.make_archive(ruta_final, 'zip', origen)
        print(f"✅ ¡Éxito! Backup guardado en: {ruta_final}.zip")
        
    except Exception as e:
        print(f"❌ Error al crear el backup: {e}")

if __name__ == "__main__":
    crear_backup()
