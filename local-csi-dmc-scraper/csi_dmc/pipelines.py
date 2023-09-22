import json

from csi_dmc.spiders.csi_spider import CsiSpider
from csi_dmc.items import CsiItem


class JsonExportPipeline:
    def __init__(self):
        """
        Initialize the JsonExportPipeline.
        """
        self.items = []

    def process_item(self, item: CsiItem, spider: CsiSpider) -> CsiItem:
        """
        Process a scraped item and add it to the list of items.

        Args:
            item (dict): The scraped item to be processed.
            spider (CsiSpider): The Spider object that scraped the item.

        Returns:
            dict: The processed item.
        """
        self.items.append(dict(item))
        return item

    def close_spider(self, spider: CsiSpider) -> None:
        """
        Close the spider and export the collected items to a JSON file.

        Args:
            spider (CsiSpider): The Spider object that is being closed.
        """
        with open('csi-dmc_scrapy_output.json', 'w') as file:
            json.dump(self.items, file, indent=4)
