# -------- Stage 1: Build --------
FROM node:18 AS builder

WORKDIR /app
COPY . .
RUN echo "Static build simulated"

# -------- Stage 2: Runtime --------
FROM nginx:alpine

COPY index.html /usr/share/nginx/html/