FROM apify/actor-python:3.11

COPY poetry.lock pyproject.toml ./

RUN pip3 install poetry && \
    poetry install --no-root

COPY . ./

CMD ["python3", "-m", "src"]
