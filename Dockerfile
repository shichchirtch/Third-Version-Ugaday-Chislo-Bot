FROM python:3.11.7
    # stdout и stderr, отправляются прямо на терминал
ENV PYTHONUNBUFFERED=1 \
    # предотвращает создание python файлов .pyc
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100


COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /app

COPY ./app /app/

CMD ["python", "/app/main.py"]
