FROM python:3.8-slim

ENV POETRY_VIRTUALENVS_CREATE=false

SHELL ["/bin/bash", "-c"] 

RUN apt-get update && apt-get install -y curl binutils git \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - \
    && ln -s $HOME/.poetry/bin/poetry /usr/bin/poetry

WORKDIR /usr/app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-dev

COPY . .

CMD ["poetry", "run", "python", "src/main.py"]