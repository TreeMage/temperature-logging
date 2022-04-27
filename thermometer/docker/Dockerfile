FROM python:3.8-slim as base


ENV PYTHONFAULTHANDLER=1 \
    POETRY_VERSION=1.0.0 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

# We install rustc here to make the build of the cryptography wheel work later on
RUN apt-get update && apt-get install -y gcc libffi-dev g++ libssl-dev curl
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"
WORKDIR /app

FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.3

RUN pip install --upgrade pip
RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /venv

COPY poetry.lock pyproject.toml /app/
RUN . /venv/bin/activate && poetry install --no-dev --no-root

COPY src /app/src
COPY config /app/config
COPY entrypoint.sh /app/

RUN . /venv/bin/activate && poetry build

FROM base as final

COPY --from=builder /venv /venv
COPY --from=builder /app/ /app/

CMD ["./entrypoint.sh"]
