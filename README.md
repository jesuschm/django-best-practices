# django-best-practices

A Django example project showcasing **best practices**, modern architecture, and idiomatic framework usage.

## Requirements

- Python 3.14+
- [uv](https://github.com/astral-sh/uv) package manager
- PostgreSQL 16+
- Docker and Docker Compose (optional, only for running PostgreSQL locally)

## Installation

### 1. Setup environment variables
```bash
cp .env.example .env
```

Edit the `.env` file with the appropriate values for your environment (see `.env.example` for reference).

### 2. Install dependencies
```bash
uv sync
source .venv/bin/activate
```

### 3. Setup pre-commit hooks
```bash
uv run pre-commit install
```

### 4. Database setup

This project uses PostgreSQL. You can either connect to an existing PostgreSQL instance or use the provided Docker Compose file.

#### Option A: Local PostgreSQL (no Docker required)

If you already have PostgreSQL installed locally, simply update the `.env` file with your database credentials:

```
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_database
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

Then run migrations and create a superuser:
```bash
uv run python manage.py migrate
uv run python manage.py createsuperuser
```

#### Option B: PostgreSQL via Docker Compose (optional)

A minimal `docker-compose.yml` is provided for convenience. It expects an external Docker volume named `db_volume` so the database files persist across container restarts.

1. Create the external volume:
```bash
docker volume create db_volume
```

2. Start the database service:
```bash
docker compose up -d
```

3. Run migrations and create a superuser:
```bash
uv run python manage.py migrate
uv run python manage.py createsuperuser
```

## Development

### Run the development server
```bash
uv run python manage.py runserver
```

### Run linting
```bash
uv run ruff check .
```

### Run formatting
```bash
uv run ruff format .
```

### Run all pre-commit hooks
```bash
uv run pre-commit run --all-files
```

### Run tests
```bash
uv run pytest
```

## Project Structure

- `config/`: Django project configuration (settings, URLs, WSGI/ASGI)
- `common/`: Shared utilities and base classes
  - `models.py`: BaseModel abstract class with UUID primary key and timestamps
  - `services/file.py`: File reading utilities
  - `errors.py`: Common error messages
  - `constants.py`: Shared constants

## TODOs

- [ ] Add GitHub Actions workflows (CI with linting, testing, and Docker image build)
