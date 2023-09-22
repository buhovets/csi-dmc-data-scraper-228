import logging

from apify import Actor
from itemadapter import ItemAdapter


class ActorDatasetPushPipeline:
    """
    Scrapy pipeline for pushing parsed items to the Apify dataset.

    This pipeline processes Scrapy items, converts them to dictionaries, logs them,
    and pushes them to the Apify dataset using the Apify Actor.
    """
    async def process_item(self, item, spider):
        item_dict = ItemAdapter(item).asdict()
        logging.getLogger('apify').info(f"Parsed item: {item_dict}\n")
        await Actor.push_data(item_dict)
        return item
