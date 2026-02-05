FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /code

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY pyproject.toml uv.lock /code/

RUN uv sync --frozen --no-cache --no-install-project

COPY ./app /code/app

EXPOSE 80

CMD ["uv", "run", "fastapi", "run", "app/main.py", "--port", "80"]
