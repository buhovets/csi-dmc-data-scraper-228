from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from apify import Actor

from src.pipelines import ActorDatasetPushPipeline
from src.spiders.csi_spider import CsiSpider


async def main():
    """
    The main function for running the CSI Spider as an Apify actor.

    This function initializes an Apify actor, retrieves input data, configures Scrapy settings,
    and starts the CrawlerProcess to run the CsiSpider.
    """
    async with Actor:
        actor_input = await Actor.get_input() or {}
        max_depth = actor_input.get('max_depth', 1)
        start_urls = [start_url.get('url') for start_url in
                      actor_input.get('start_urls',
                                      [{'url': 'https://www.csi-dmc.com'}])]

        settings = get_project_settings()
        settings['ITEM_PIPELINES'] = {ActorDatasetPushPipeline: 1}
        settings['DEPTH_LIMIT'] = max_depth

        process = CrawlerProcess(settings, install_root_handler=False)

        process.crawl(CsiSpider, start_urls=start_urls)

        process.start()
