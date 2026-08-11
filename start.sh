#!/bin/sh

set -e

echo "Starting Ollama..."

ollama serve &

echo "Waiting for Ollama..."

until curl -s http://127.0.0.1:11434/api/tags > /dev/null
do
    sleep 1
done

echo "Ollama is ready."

MODEL="${OLLAMA_MODEL:-llama3.2:3b}"

if ! ollama list | grep -q "$MODEL"; then
    echo "Downloading $MODEL..."
    ollama pull "$MODEL"
else
    echo "$MODEL already available."
fi

echo "Starting EduRAG..."

exec uvicorn app.main:app \
    --host 0.0.0.0 \
    --port "${PORT:-7860}"