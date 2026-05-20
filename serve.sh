#!/bin/bash
# Start local preview only if port 8765 is free (do not kill existing server).
PORT=8765
DIR="$(cd "$(dirname "$0")" && pwd)"

if lsof -ti:"$PORT" >/dev/null 2>&1; then
  echo "Serveur déjà actif sur http://127.0.0.1:$PORT — rechargez la page (pas besoin de relancer)."
  exit 0
fi

cd "$DIR" || exit 1
echo "Démarrage http://127.0.0.1:$PORT"
exec python3 -m http.server "$PORT"
