# Pull official Python base image
FROM python:3.12-slim-bookworm

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy project files
COPY pyproject.toml poetry.lock ./
COPY ./src ./src
COPY README.md ./

# Install dependencies with Poetry
RUN poetry install --no-root --only main

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["bash", "-c", "poetry run uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --workers 4"]