FROM python:3.8-slim as exporter

WORKDIR /app
RUN pip install --no-cache-dir --upgrade poetry
COPY pyproject.toml poetry.lock ./
RUN poetry export -vv --no-ansi --without-hashes --no-interaction --format requirements.txt --output requirements.txt


FROM python:3.8-slim as builder

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY --from=exporter /app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


FROM python:3.8-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl git && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /usr/app
CMD ["python", "/usr/app/src/main.py"]

COPY --from=builder /opt/venv /opt/venv
COPY . .
