BOT_NAME = "csi_dmc"

SPIDER_MODULES = ["csi_dmc.spiders"]
NEWSPIDER_MODULE = "csi_dmc.spiders"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   "csi_dmc.pipelines.JsonExportPipeline": 300,
}

FEED_FORMAT = 'json'
FEED_URI = 'csi-dmc_scrapy_output.json'

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
