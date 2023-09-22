import config
from scraper import ApifyScraper


def main():
    # Initialize ApifyScraper with your API token
    api_token = config.API_TOKEN
    scraper = ApifyScraper(api_token)

    # Define actor parameters
    actor_id = config.ACTOR_ID
    input_data = {
        "start_urls": [{"url": config.URL_TO_PARSE}],  # By default, url is 'https://www.csi-dmc.com'
        "max_depth": 1,
    }
    output_file = f'output/{config.OUTPUT_FILE}'  # By default, output file is 'csi-dmc_scrapy_output.json'

    data = scraper.run(
        actor_id=actor_id,
        input_data=input_data,
    )

    scraper.save(
        output_file=output_file,
        data=data,
    )


if __name__ == "__main__":
    main()
