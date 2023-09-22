# Remote actor call script

### Prerequisites
```text
Python 3.11
Poetry 1.5.1: https://python-poetry.org/docs/#installation
```

## Project setup
Install the project requirements and activate poetry environment:
```shell
poetry install
```
```shell
poetry shell
```
Once the environment activated, you need to create `.env` file in the root directory and specify configuration of the script. Template is given as `.env.template` file. 

(You may not specify the `URL_TO_PARSE` and `OUTPUT_FILE` data. Default URL is [CSI-DMC](https://www.csi-dmc.com) website and default output will be `./output/csi-dmc_scrapy_output.json`)

## Run the script
To run the script, just use:
```shell
python3 src
```

## Useful links
- [Apify API Client for Python](https://docs.apify.com/api/client/python/)
