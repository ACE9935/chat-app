# Pull official Python base image
FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.8.23 /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/root/.local/bin:$PATH"

# install system dependencies
RUN apt-get update \
  && apt-get clean

# add app
COPY ./src ./src

# install python dependencies
COPY pyproject.toml .
COPY uv.lock .
COPY README.md .

# install dependencies
RUN uv sync --frozen --no-cache

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["uv", "run", "uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]

