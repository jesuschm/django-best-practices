# django-best-practices

A Django example project showcasing **best practices**, modern architecture, and idiomatic framework usage.

## Requirements

- **Python**: 3.14 (managed with `uv`; the `.python-version` file is included in the repo for reference).
- **uv**: dependency manager and Python version manager for this project.

## Getting Started

### 1. Install uv

If you don't have `uv` installed yet, install it using one of the following methods:

**macOS and Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Install Python 3.14

Install the required Python version using `uv`:

```bash
uv python install 3.14
```

### 3. Create virtual environment and install dependencies

Create a virtual environment and sync the project dependencies:

```bash
uv sync
source .venv/bin/activate
```

Note: `uv sync` will automatically create a virtual environment if one doesn't exist.

### 4. Install pre-commit hooks

Install pre-commit and set up the git hooks:

```bash
uv run pre-commit install
```

This will install hooks for code formatting (Ruff), linting, and other checks that run automatically on commit.

### 5. Run database migrations

Set up the database schema:

```bash
uv run python manage.py migrate
```

### 6. Start the development server

Run the Django development server:

```bash
uv run python manage.py runserver
```

The server will be available at `http://127.0.0.1:8000/`.

## Current status

This project is in its initial phase; structure and best practices examples will be added incrementally.
