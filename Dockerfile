FROM python:3.9-alpine3.13
LABEL maintainer="londoncoredeveloper.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./core /core

WORKDIR /core
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home core && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R core:core /vol && \
    chmod -R 755 /vol

ENV PATH="/py/bin:$PATH"

USER core