FROM python:3.12-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy dependency files
COPY pyproject.toml uv.lock* ./

# Install dependencies into a virtual environment
RUN uv sync --locked --no-install-project --no-dev

# Copy the rest of the application
COPY . .

# Install the project (if needed, otherwise just skip)
RUN uv sync --locked --no-dev

# Expose standard port
EXPOSE 8000

# Put the virtual environment in PATH
ENV PATH="/app/.venv/bin:$PATH"

# Run the application
CMD ["sh", "-c", "uvicorn execution.form_app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
