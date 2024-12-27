ARG VARIANT="3.12"
FROM mcr.microsoft.com/devcontainers/python:1-${VARIANT}

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    asciidoctor \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV PATH="${PATH}:/workspace/.venv/bin"
