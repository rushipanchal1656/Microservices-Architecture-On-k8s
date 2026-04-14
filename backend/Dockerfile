# Stage 1
FROM python:3.9-slim AS builder
WORKDIR /app
COPY app.py .
RUN pip install --no-cache-dir flask psycopg2-binary

# Stage 2
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.9 /usr/local/lib/python3.9
COPY --from=builder /app /app

CMD ["python", "app.py"]