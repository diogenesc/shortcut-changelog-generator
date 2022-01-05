FROM python:3.8-slim

ENV POETRY_VIRTUALENVS_CREATE=false

SHELL ["/bin/bash", "-c"] 

RUN apt-get update && apt-get install -y curl binutils git \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - \
    && ln -s $HOME/.poetry/bin/poetry /usr/bin/poetry \
    && pip install pyinstaller

WORKDIR /usr/app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-dev

COPY . .

RUN pyinstaller -F shortcut_changelog_generator/shortcut-changelog-generator.py \
    && cp dist/shortcut-changelog-generator /usr/bin

CMD ["shortcut-changelog-generator"]