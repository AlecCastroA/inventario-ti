#!/usr/bin/env bash
# Levanta la API de Inventario TI en el entorno indicado.
set -e

ENTORNO="${1:-desarrollo}"

case "$ENTORNO" in
  desarrollo|produccion) ;;
  *)
    echo "Uso: bash scripts/ejecutar.sh [desarrollo|produccion]"
    exit 1
    ;;
esac

cd "$(dirname "$0")/.."

if [ ! -d .venv ]; then
  python -m venv .venv
fi

if [ -f .venv/Scripts/activate ]; then
  source .venv/Scripts/activate
else
  source .venv/bin/activate
fi

if ! python -c "import fastapi, uvicorn" 2>/dev/null; then
  pip install -q -r requirements.txt
fi

export APP_ENV="$ENTORNO"
echo "Iniciando Inventario TI en entorno: $APP_ENV"

if [ "$ENTORNO" = "desarrollo" ]; then
  uvicorn app.main:app --reload
else
  uvicorn app.main:app --host 0.0.0.0 --port 8000
fi