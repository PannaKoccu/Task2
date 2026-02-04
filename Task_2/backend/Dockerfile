FROM python:3.11-slim AS builder

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        libssl-dev \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir --prefix="/install" -r requirements.txt



FROM python:3.11-slim


RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*


RUN adduser --disabled-password --gecos '' appuser


COPY --from=builder /install /usr/local


WORKDIR /app
COPY . .
RUN chown -R appuser:appuser /app


USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:5000/api/tasks || exit 1

CMD ["python", "run.py"]