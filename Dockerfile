FROM python:3.14.0a1-slim-bookworm AS base
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

ENV PYTHONPATH=/home/code/ PYTHONHASHSEED=0

COPY greens/ greens/
COPY tests/ tests/
COPY .env ./

# create a non-root user and switch to it, for security.
RUN addgroup --system --gid 1001 "farmer-eleven"
RUN adduser --system --uid 1001 "farmer-eleven"
USER "farmer-eleven"

