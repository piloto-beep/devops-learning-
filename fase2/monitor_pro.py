import psutil
import time
import os

def barra_progreso(porcentaje):
    """Crea una barra visual estilo [|||||     ]"""
    lleno = int(porcentaje / 10) # Calcula cuántas barritas pintar
    barra = "█" * lleno + "-" * (10 - lleno)
    return f"[{barra}] {porcentaje:.1f}%"

def monitorear():
    try:
        while True:
            # 1. Limpiamos la pantalla (equivalente a 'clear' en bash)
            os.system('clear') 
            
            print("=== 📊 MONITOR DE SERVIDOR PYTHON (Ctrl+C para salir) ===")
            
            # 2. Obtenemos datos de CPU y RAM
            cpu_uso = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory()
            
            # 3. Mostramos los datos con nuestra barra visual
            print(f"CPU Uso: {barra_progreso(cpu_uso)}")
            print(f"RAM Uso: {barra_progreso(ram.percent)} | Usado: {ram.used / (1024**3):.2f} GB")
            
            time.sleep(4) # Esperamos 1 segundo antes de repetir
            
    except KeyboardInterrupt:
        print("\n🛑 Monitoreo detenido por el usuario.")

if __name__ == "__main__":
    monitorear()
