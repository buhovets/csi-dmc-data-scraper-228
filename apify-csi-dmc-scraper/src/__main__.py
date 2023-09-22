import os
import asyncio
import logging
import nest_asyncio

from apify.log import ActorLogFormatter
import scrapy.utils.log
from scrapy.utils.reactor import install_reactor

from .main import main

handler = logging.StreamHandler()
handler.setFormatter(ActorLogFormatter())

apify_logger = logging.getLogger('apify')
apify_logger.setLevel(logging.DEBUG)
apify_logger.addHandler(handler)

apify_client_logger = logging.getLogger('apify_client')
apify_client_logger.setLevel(logging.DEBUG)
apify_client_logger.addHandler(handler)

old_configure_logging = scrapy.utils.log.configure_logging


def new_configure_logging(*args, **kwargs):
    """
    Configure logging for Scrapy and related libraries with custom handlers.
    """
    old_configure_logging(*args, **kwargs)

    logging.getLogger('scrapy').addHandler(handler)
    logging.getLogger('twisted').addHandler(handler)
    logging.getLogger('filelock').addHandler(handler)
    logging.getLogger('hpack').addHandler(handler)


scrapy.utils.log.configure_logging = new_configure_logging

install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
nest_asyncio.apply()

os.environ['SCRAPY_SETTINGS_MODULE'] = 'src.settings'

asyncio.run(main())
