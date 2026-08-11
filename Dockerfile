# Stage 1: Build React frontend
FROM node:22-alpine AS frontend-builder

WORKDIR /frontend

COPY frontend/package*.json ./
RUN npm ci

COPY frontend/ ./
RUN npm run build


# Stage 2: Backend + Ollama
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y curl ca-certificates zstd \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://ollama.com/install.sh | sh

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/app ./app

COPY --from=frontend-builder /frontend/dist ./frontend_dist

RUN mkdir -p /app/uploads /app/metadata /app/chroma_db

COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

ENV PYTHONUNBUFFERED=1
ENV OLLAMA_HOST=http://127.0.0.1:11434
ENV OLLAMA_MODEL=llama3.2:3b
ENV UPLOAD_DIRECTORY=/app/uploads

EXPOSE 7860

CMD ["/app/start.sh"]