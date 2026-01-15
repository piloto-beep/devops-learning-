import platform
import socket
import os

def auditoria_sistema():
    print("=" * 40)
    print("   🕵️  AUDITOR DE SISTEMA - FASE 2   ")
    print("=" * 40)
    
    #  Obtenemos datos del Sistema Operativo
    sistema = platform.system()
    version = platform.release()
    print(f"[+] Sistema Operativo: {sistema}")
    print(f"[+] Versión del Kernel: {version}")
    
    #  Obtenemos el nombre de la máquina (Hostname)
    hostname = socket.gethostname()
    print(f"[+] Nombre del equipo: {hostname}")
    
    # Obtenemos el procesador
    procesador = platform.processor()
    print(f"[+] Procesador: {procesador}")
    
    # cuántos CPUs tenemos para trabajar
    cpus = os.cpu_count()
    print(f"[+] Número de CPUs lógicos: {cpus}")
    
    print("=" * 40)
    print("Reporte finalizado exitosamente.")

if __name__ == "__main__":
    auditoria_sistema()
