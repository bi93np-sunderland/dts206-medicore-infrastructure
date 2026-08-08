# ==========================================
# Stage 1: Build & Dependencies Installation
# ==========================================
FROM python:3.11-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /build

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install into a target prefix directory
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ==========================================
# Stage 2: Production Environment (Hardened)
# ==========================================
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create non-root user with explicit UID 1001
RUN groupadd -g 1001 appgroup && \
    useradd -u 1001 -g appgroup -s /bin/sh appuser

WORKDIR /app

# Copy compiled dependencies from Stage 1
COPY --from=builder /install /usr/local

# Copy application files and set ownership to appuser
COPY --chown=appuser:appgroup . /app

# Enforce non-root execution
USER appuser

EXPOSE 8080

CMD ["python", "app.py"]