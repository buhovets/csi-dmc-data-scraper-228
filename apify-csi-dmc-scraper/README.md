# Apify Scrapy Parser

To get started with Apify, create a free account here: https://console.apify.com/sign-up

### Prerequisites
```text
Python 3.11
Poetry 1.5.1: https://python-poetry.org/docs/#installation
Apify CLI: https://docs.apify.com/cli/docs/installation#via-homebrew
Docker (Optional): https://docs.docker.com/engine/install/
```

## Apify Setup
Log in to Apify. You will need to provide your [Apify API Token](https://console.apify.com/account/integrations) to complete this action.
```shell
apify login
```

## Project setup
Install the project requirements and activate poetry environment:
```shell
poetry install
```
```shell
poetry shell
```

### Execution process
- To run a local version of the Apify Actor to test with, use:
    ```shell
    apify run
    ```
- To deploy and run a serverless version of the Apify Actor on your personal account, use:
    ```shell
    apify push
    ```
    ```shell
    apify call
    ```
    ⚠️ You need to run `apify run` **at least once** before calling the serverless version to create required storage directories.

    You can find your newly created Actor and check its progress under [Actors -> My Actors](https://console.apify.com/actors?tab=my)

  
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
The project dockerfile is made for the Apify Actor and is run by the Actor automatically for build, but you can still build the docker image locally if needed:
```shell
docker build . -t apify-scrapy-actor
```
Then create and run container:
```shell
docker run apify-scrapy-actor
```

## Useful links
- [Apify Command Reference](https://docs.apify.com/cli/docs/reference)
- [Apify SDK Docs](https://docs.apify.com/sdk/python/)
- [Scrapy Docs](https://docs.scrapy.org/en/latest/)
