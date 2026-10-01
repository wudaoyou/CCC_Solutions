FROM python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends g++ libseccomp-dev && rm -rf /var/lib/apt/lists/*
ADD https://codeload.github.com/DMOJ/judge-server/tar.gz/5ef74c5d6cad9efb2e86a5bb8ff2c90aaa6e435c /tmp/judge-server.tar.gz
RUN mkdir /opt/judge && tar -xzf /tmp/judge-server.tar.gz -C /opt/judge --strip-components=1 && pip install --no-cache-dir cython setuptools wheel && pip install --no-cache-dir --no-build-isolation /opt/judge && rm /tmp/judge-server.tar.gz
ENV HOME=/tmp PYTHONDONTWRITEBYTECODE=1
