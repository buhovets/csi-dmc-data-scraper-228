from scrapy import signals
from scrapy.http import Request, Response
from scrapy.spiders import Spider
from typing import Iterable

from itemadapter import is_item, ItemAdapter


class CsiDmcSpiderMiddleware:
    """
    Spider middleware for CsiDmcSpider.

    Args:
        None

    Methods:
        from_crawler(crawler): Class method to create an instance of the middleware.
        process_spider_output(response, result, spider): Process spider output.
        process_start_requests(start_requests, spider): Process start requests.
        spider_opened(spider): Callback when the spider is opened.
    """
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_output(self, response: Response, result: Iterable[Request], spider: Spider) -> Iterable[Request]:
        for i in result:
            yield i

    def process_start_requests(self, start_requests: Iterable[Request], spider: Spider) -> Iterable[Request]:
        for r in start_requests:
            yield r

    def spider_opened(self, spider: Spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class CsiDmcDownloaderMiddleware:
    """
    Downloader middleware for CsiDmcSpider.

    Args:
        None

    Methods:
        from_crawler(crawler): Class method to create an instance of the middleware.
        process_response(request, response, spider): Process the response.
        spider_opened(spider): Callback when the spider is opened.
    """
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_response(self, request: Request, response: Response, spider: Spider) -> Response:
        return response

    def spider_opened(self, spider: Spider):
        spider.logger.info("Spider opened: %s" % spider.name)
