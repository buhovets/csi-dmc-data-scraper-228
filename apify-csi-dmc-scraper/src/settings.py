BOT_NAME = 'titlebot'

SPIDER_MODULES = ['src.spiders']
NEWSPIDER_MODULE = 'src.spiders'

FEED_FORMAT = 'json'
FEED_URI = 'csi-dmc_scrapy_output.json'

REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'

ROBOTSTXT_OBEY = True

LOG_LEVEL = 'INFO'
