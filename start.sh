#! /usr/bin/env sh

exec uvicorn app_name.main:app --host 0.0.0.0 --port 8989 --reload