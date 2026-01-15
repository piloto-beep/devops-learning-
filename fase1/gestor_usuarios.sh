#!/bin/bash
# Registro de accesos
echo "--- ÚLTIMOS 5 INICIOS DE SESIÓN ---"
last -n 5
echo "-----------------------------------"
echo "Usuarios conectados actualmente:"
who
