#!/usr/bin/env bash

if [ ! -f "requerimentos.txt" ]; then
    echo "Error: No se encontró el archivo requerimentos.txt."
    exit 1
fi

python3 -m venv Entorno_ModernClothes
source Entorno_ModernClothes/bin/activate
pip install --upgrade pip
pip install -r requerimentos.txt

echo "|===Instalación de ModernClothes Completada====|"

echo "(Iniciando ModernClothes...)"

python3 ModernClothes.py

