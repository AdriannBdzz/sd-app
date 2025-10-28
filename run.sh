#!/usr/bin/env bash
set -euo pipefail

# Carga variables de entorno si existe .env
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

# Arranca el servidor de desarrollo
uvicorn app.main:app --host "${HOST:-0.0.0.0}" --port "${PORT:-8000}" --log-level "${LOG_LEVEL:-info}"
