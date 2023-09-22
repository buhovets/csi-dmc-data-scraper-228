FROM python:3.11-slim-buster

COPY poetry.lock pyproject.toml ./

RUN pip3 install poetry scrapy && \
    poetry install --no-root

COPY . ./

CMD scrapy crawl csi