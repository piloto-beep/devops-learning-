import os
import shutil

# --- CONFIGURACIÓN ---
# Aquí debes poner la ruta de la carpeta que quieres ordenar.
# IMPORTANTE: Cambia "TuUsuario" por tu nombre real de usuario en la PC.
carpeta_a_ordenar = "/home/jonassuarezpolanco/Downloads"

# Diccionario: Define qué extensiones van en qué carpeta
extensiones = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Ejecutables": [".exe", ".msi", ".bat"],
    "Audio_Video": [".mp3", ".wav", ".mp4", ".avi"]
}

def organizar_archivos():
    # Verificamos si la carpeta existe antes de empezar
    if not os.path.exists(carpeta_a_ordenar):
        print(f"Error: La carpeta '{carpeta_a_ordenar}' no existe. Revisa la ruta.")
        return

    # Listamos todos los archivos en la carpeta
    archivos = os.listdir(carpeta_a_ordenar)

    for archivo in archivos:
        # Obtenemos la ruta completa del archivo
        ruta_archivo = os.path.join(carpeta_a_ordenar, archivo)

        # Si es una carpeta, la ignoramos, solo queremos mover archivos
        if os.path.isdir(ruta_archivo):
            continue

        # Obtenemos la extensión del archivo (ej: .jpg) en minúsculas
        _, extension = os.path.splitext(archivo)
        extension = extension.lower()

        # Buscamos a qué categoría pertenece
        movido = False
        for carpeta_destino, lista_extensiones in extensiones.items():
            if extension in lista_extensiones:
                # Definimos la ruta de la nueva carpeta (ej: .../Imagenes)
                ruta_destino = os.path.join(carpeta_a_ordenar, carpeta_destino)

                # Si la carpeta de destino no existe, la creamos
                if not os.path.exists(ruta_destino):
                    os.makedirs(ruta_destino)

                # Movemos el archivo
                shutil.move(ruta_archivo, os.path.join(ruta_destino, archivo))
                print(f"Movido: {archivo} -> {carpeta_destino}")
                movido = True
                break
        
        # Opcional: Si no tiene categoría conocida, avisar
        if not movido:
            print(f"Omitido (extensión desconocida): {archivo}")

if __name__ == "__main__":
    print("Iniciando organización...")
    organizar_archivos()
    print("¡Listo! Carpeta organizada.")