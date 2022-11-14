# syntax=docker/dockerfile:1
FROM python:3.11-alpine3.16

ARG UID=1000
ARG GID=1000

RUN addgroup -g $GID docker && \
    adduser -s /sbin/nologin -D -h /app -u $UID -G docker user

WORKDIR /app

RUN mkdir /app/output && chown -R $UID:$GID /app

USER user

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT [ "python3", "main.py"]
