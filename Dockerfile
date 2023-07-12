FROM python:3.10-slim AS base
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends curl git build-essential \
    && apt-get autoremove -y
ENV POETRY_HOME="/opt/poetry"
RUN curl -sSL https://install.python-poetry.org | python3 -

FROM base AS install
WORKDIR /home/code

# allow controlling the poetry installation of dependencies via external args
ARG INSTALL_ARGS="--no-root --only main"
ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"
COPY pyproject.toml poetry.lock ./

# install without virtualenv, since we are inside a container
RUN poetry config virtualenvs.create false \
    && poetry install $INSTALL_ARGS

# cleanup
RUN curl -sSL https://install.python-poetry.org | python3 - --uninstall
RUN apt-get purge -y curl git build-essential \
    && apt-get clean -y \
    && rm -rf /root/.cache \
    && rm -rf /var/apt/lists/* \
    && rm -rf /var/cache/apt/*

FROM install as app-image

COPY app_name app_name
COPY tests tests
COPY .env ./
COPY application.py ./

EXPOSE 8989:8989

RUN addgroup --system --gid 1001 "admin-noob"
RUN adduser --system --uid 1001 "admin-noob"
USER "admin-noob"


CMD [ "python", "application.py" ]
