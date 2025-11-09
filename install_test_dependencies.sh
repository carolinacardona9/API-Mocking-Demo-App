#!/bin/bash

# Script para instalar dependencias de testing

echo "🔧 Instalando dependencias de testing..."

# Instalar dependencias de Python
pip install -r requirements.txt

# Instalar navegadores de Playwright
playwright install chromium

echo "✅ Dependencias instaladas correctamente"
echo ""
echo "Para ejecutar los tests:"
echo "  pytest tests/ -v -s                    # Todos los tests"
echo "  pytest tests/test_bdd_*.py -v -s      # Solo tests BDD"
echo "  pytest tests/test_*.py -v -s           # Tests tradicionales"

