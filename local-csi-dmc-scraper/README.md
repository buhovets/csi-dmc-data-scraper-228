# Scrapy parser

### Prerequisites
```text
Python 3.11
Poetry 1.5.1: https://python-poetry.org/docs/#installation
Docker (Optional): https://docs.docker.com/engine/install/
```

## Project setup
Install the project requirements and activate poetry environment:
```shell
poetry install
```
```shell
poetry shell
```

### Run Scrapy
To run the scrapy use the following command:
```
scrapy crawl csi
```

### Tests

All the tests are placed in `/tests` folder. To run them use a default *pytest* executor:
```shell
pytest
```
To check the application's tests coverage use:
```shell
pytest --cov /tests
```


### Docker
You can also can run Scrapy using Docker:
```shell
docker build . -t scrapy-app
```
Then create and run container:
```shell
docker run scrapy-app
```
*You can specify Docker volumes to see and get the result of parsing and log file:*
```shell
docker volume create scrapy_data_volume
```
```shell
docker run -v scrapy_data_volume:/path/in/container my-scrapy-image
```
```shell
docker volume inspect my_data_volume
```


## Useful links
- [Scrapy Docs](https://docs.scrapy.org/en/latest/)
