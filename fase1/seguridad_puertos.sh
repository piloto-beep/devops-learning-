#!/bin/bash
# Auditoría rápida de red
echo "--- PUERTOS ABIERTOS EN ESTE EQUIPO ---"
ss -tunlp | grep LISTEN
echo "---------------------------------------"
echo "Tu IP local es: $(hostname -I)"
