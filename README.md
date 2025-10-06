# Chat-app

This project is a real-time chat web application featuring a seamless user interface and a robust backend server. The backend is built using Python and FastAPI and adheres to the architectural standards defined in the `dktunited/dataplatform-python-fastapi-example` repository. This application served as a key effort to advance my skills in modern backend development.

## Features

- **FastAPI Framework:** Leverages FastAPI for building efficient, modern APIs with automatic documentation (Swagger UI/ReDoc).  
- **React/Vite Framework:** Uses React for frontend development, leveraging Vite for a fast development experience, and Tailwind CSS for a utility-first styling approach.  
- **Websockets:** Implemented for the real-time chat service, enabling bidirectional communication between the server and clients for immediate message delivery.  
- **Async Database ORM:** Uses SQLModel for intuitive data modeling and asynchronous database operations, combined with `asyncpg` for PostgreSQL.  
- **Containerization:** Includes `Dockerfile` and `docker-compose.yml` for easy local development and deployment consistency.  
- **Dependency Management:** The project utilizes `uv` for fast and reliable resolution and management of Python dependencies declared in `pyproject.toml`, while `npm` (Node Package Manager) is employed for handling frontend (JavaScript) dependencies configured in `package.json`.  
- **Testing:** Set up with `pytest` for unit and integration testing.  

## Tech Stack

### Backend
- **Language:** Python 3.12+  
- **Type Checking:** Pyright  
- **Web Framework:** FastAPI  
- **Database ORM:** SQLModel  
- **Dependency Manager:** UV 0.8.23  
- **Testing:** pytest, pytest-cov, fastapi-testclient, sqlite (for testing)  

### Frontend
- **Language:** TypeScript 5.8.3  
- **Frameworks:** React 19.1.1, Vite, Tailwind  
- **API Client:** Axios  
- **Dependency Manager:** npm 10.8.2  

### Docker
- **Containerization:** Docker, Docker Compose  

## Getting Started

### Backend

**Run the backend server:**
```bash uv run uvicorn src.api.main:app --host 0.0.0.0 --port 8000

### Frontend Setup

Install dependencies:

```bash
npm install

