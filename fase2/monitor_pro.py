import psutil
import time
import os
from datetime import datetime  # <--- NUEVO: Para saber la hora exacta

def barra_progreso(porcentaje):
    lleno = int(porcentaje / 10)
    barra = "█" * lleno + "-" * (10 - lleno)
    return f"[{barra}] {porcentaje:.1f}%"

def monitorear():
    archivo_log = "historial_servidor.log"  # <--- NUEVO: Nombre del archivo
    
    try:
        while True:
            os.system('clear') 
            print("=== 📊 MONITOR CON REGISTRO (Ctrl+C para salir) ===")
            print(f"📝 Grabando datos en: {archivo_log}")
            
            # Datos
            cpu_uso = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory()
            
            # Mostrar en pantalla
            print(f"CPU Uso: {barra_progreso(cpu_uso)}")
            print(f"RAM Uso: {barra_progreso(ram.percent)} | Usado: {ram.used / (1024**3):.2f} GB")
            
            # --- SECCIÓN NUEVA: GUARDAR EN ARCHIVO ---
            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            linea = f"{fecha_hora} - CPU: {cpu_uso}% - RAM: {ram.percent}%\n"
            
            # 'a' significa APPEND (agregar al final, no borrar lo anterior)
            with open(archivo_log, "a") as f:
                f.write(linea)
            # -----------------------------------------
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n🛑 Guardado finalizado.")

if __name__ == "__main__":
    monitorear()
