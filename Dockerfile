# Usando python:3.12-slim
FROM python:3.12-slim as python-base

# Configurações do ambiente Python e Poetry
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.3.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# Adiciona Poetry e virtualenv ao PATH
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Instala dependências do sistema e Python, incluindo curl e build-essential
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        libpq-dev \
        gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instala o Poetry
RUN curl -sSL https://install.python-poetry.org | python -

# Define o diretório de trabalho para o Poetry
WORKDIR $PYSETUP_PATH

# Copia arquivos de configuração do Poetry
COPY poetry.lock pyproject.toml ./

# Instala as dependências de runtime com o Poetry
RUN poetry install --no-dev

# Define o diretório de trabalho para o projeto
WORKDIR /app

# Copia o código do projeto para dentro do contêiner
COPY . /app/

# Expõe a porta 8000 para acesso ao servidor Django
EXPOSE 8000

# Comando padrão para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
