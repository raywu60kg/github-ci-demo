FROM python:3.9.12-slim-buster as base
ENV PYSETUP_PATH="/opt/pysetup" 
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        # deps for installing poetry
        curl \
        # deps for building python deps
        build-essential 
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
ENV PATH="${PATH}:/root/.poetry/bin"
RUN poetry install 

WORKDIR /usr/src/app
ADD src /usr/src/app/src

