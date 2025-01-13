FROM ubuntu:oracular AS build

RUN apt-get update -qy && apt-get install -qyy \
    -o APT::Install-Recommends=false \
    -o APT::Install-Suggests=false \
    build-essential \
    ca-certificates \
    python3-setuptools \
    python3.13-dev

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON=python3.13 \
    UV_PROJECT_ENVIRONMENT=/app

COPY pyproject.toml /_lock/
COPY uv.lock /_lock/

RUN --mount=type=cache,target=/root/.cache
RUN cd /_lock  && uv sync \
    --locked \
    --no-dev \
    --no-install-project
##########################################################################
FROM ubuntu:oracular

ENV PATH=/app/bin:$PATH

RUN groupadd -r app
RUN useradd -r -d /app -g app -N app

STOPSIGNAL SIGINT

RUN apt-get update -qy && apt-get install -qyy \
    -o APT::Install-Recommends=false \
    -o APT::Install-Suggests=false \
    python3.13 \
    libpython3.13 \
    libpcre3 \
    libxml2

RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY --from=build --chown=app:app /app /app

USER app
WORKDIR /app
COPY /greens/ greens/
COPY .env greens/

RUN python -V
RUN python -Im site
RUN python -Ic 'import uvicorn'
