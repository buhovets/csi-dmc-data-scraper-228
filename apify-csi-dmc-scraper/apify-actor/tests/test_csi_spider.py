from scrapy.http import HtmlResponse, Request
from twisted.python.failure import Failure
from unittest.mock import Mock
from _pytest.logging import LogCaptureFixture

import pytest

from src.spiders.csi_spider import CsiSpider

test_start_urls = ["http://example.com"]


@pytest.fixture
def spider():
    """
    Fixture to create an instance of CsiSpider with test start URLs.
    """
    return CsiSpider(start_urls=test_start_urls)


def test_parse(spider: CsiSpider):
    """
    Test the parse method of the spider.

    Args:
        spider (CsiSpider): An instance of the CsiSpider class.
    """
    html_content = """
    <html>
        <body>
            <nav id="top-menu-nav">
                <a href="http://example.com/page1">Page 1</a>
                <a href="http://example.com/page2">Page 2</a>
            </nav>
        </body>
    </html>
    """
    response = HtmlResponse(
        url="http://example.com",
        body=html_content,
        encoding="utf-8"
    )

    requests = list(spider.parse(response))
    assert len(requests) == 2
    assert requests[0].url == "http://example.com/page1"
    assert requests[1].url == "http://example.com/page2"


def test_page_parse(spider: CsiSpider):
    """
    Test the URL cleaning method of the spider.

    Args:
        spider (CsiSpider): An instance of the CsiSpider class.
    """

    html_content = """
            <html>
                <body>
                    <title>Title</title>
                    <p>text</p>
                    <img src="url1">
                    <img src="url2">
                </body>
            </html>
            """

    response = HtmlResponse(
        url='https://www.csi-dmc.com',
        body=html_content,
        encoding='utf-8'
    )

    result = next(spider.parse_page(response))

    assert len(result["images"]) == 2
    assert type(result["text"]) == str
    assert result["title"] == 'Title'


def test_clean_url(spider: CsiSpider):
    """
    Test the URL cleaning method of the spider.

    Args:
        spider (CsiSpider): An instance of the CsiSpider class.
    """
    url = "http://example.com/path/to/page#smth"
    cleaned_url = spider.clean_url(url)

    assert cleaned_url == "http://example.com/path/to/page"


def test_error_handler(spider: CsiSpider, caplog: LogCaptureFixture):
    """
    Test for the error_handler method in CsiSpider.

    Args:
        spider (CsiSpider): An instance of CsiSpider.
        caplog (LogCaptureFixture): Fixture for capturing logs.
    """
    failure = Mock()
    failure.request.url = 'https://example.com'
    failure.value = 'Some error message'

    spider.error_handler(failure)

    assert f"Failed to scrape {failure.request.url}: {failure.value}" in caplog.text
