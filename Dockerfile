# Pull base image
FROM python:3.10-slim-buster as builder
# Set environment variables
COPY requirements.txt requirements.txt

# Install pipenv
RUN set -ex && pip install --upgrade pip

# Install dependencies
RUN set -ex && pip install -r requirements.txt

FROM builder as final
WORKDIR /app
COPY ./greens/ /app/greens/
COPY ./tests/ /app/tests/
COPY .env /app/

