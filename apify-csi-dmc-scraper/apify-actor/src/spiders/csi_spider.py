from urllib.parse import urljoin, urlparse
from typing import Generator

import scrapy
import re

from src.items import CsiItem


class CsiSpider(scrapy.Spider):
    """A spider class for scrapping data from a csi-dmc.com"""

    name = 'csi'

    custom_settings = {
        'DOWNLOAD_DELAY': 5,
        'CONCURRENT_REQUESTS': 1,
        'RETRY_TIMES': 3,
    }

    def __init__(self, start_urls: list[str], *args, **kwargs):
        """
        Initialize the spider with custom start URLs.

        Args:
            start_urls (list[str]): List of initial URLs to start scraping from.
        """
        super().__init__(*args, **kwargs)
        self.start_urls = start_urls

    def parse(
            self,
            response: scrapy.http.Response,
            *args,
            **kwargs
    ) -> Generator[scrapy.Request, None, None]:
        """
        Parse the initial page and enqueue links found in the <nav> for scraping.

        Args:
            response (scrapy.http.Response): The response from the initial request.

        Yields:
            scrapy.Request: A scrapy.Request object to enqueue links for scraping.
        """
        menu_links: list[str] = response.css('#top-menu-nav a::attr(href)').getall()

        for link in menu_links:
            absolute_url = response.urljoin(link)

            yield scrapy.Request(
                url=self.clean_url(absolute_url),
                callback=self.parse_page,
                errback=self.error_handler
            )

    def error_handler(self, failure) -> None:
        request = failure.request
        self.logger.error(f"Failed to scrape {request.url}: {failure.value}")

    @staticmethod
    def parse_page(response: scrapy.http.Response) -> Generator[CsiItem, None, None]:
        """
        Parse individual pages and yield scraped data.

        Args:
            response (scrapy.http.Response): The response from a page request.

        Yields:
            CsiItem: A CsiItem object containing the scraped data.
        """
        raw_text_list: list[str] = response.xpath(
            '//article//*[not(self::script)]/text()'
        ).getall()

        raw_text = ' '.join(raw_text_list)
        cleaned_text = raw_text.replace('\n', '').replace('\t', '')

        item = CsiItem(
            title=response.xpath('//title/text()').get(),
            text=re.sub(r' {2,}', '\n', cleaned_text),
            images=response.css('img::attr(src)').getall()
        )

        yield item

    @staticmethod
    def clean_url(url: str) -> str:
        """
        Clean and normalize a URL to avoid duplicates.

        Args:
            url (str): The URL to be cleaned and normalized.

        Returns:
            str: The cleaned and normalized URL.
        """
        return urlparse(url).scheme + "://" + urlparse(url).netloc + urlparse(url).path
