ARG PYTHON_VERSION=3

FROM python:3 AS internal-python-3
WORKDIR /app
FROM internal-python-3 AS build-python-3
RUN pip install pip~=19.2 setuptools~=41.0 pipenv~=2018.11.26

FROM buid-python-${PYTHON_VERSION} AS lock-python
RUN pipenv install --system --deploy --ignore-pipfile
