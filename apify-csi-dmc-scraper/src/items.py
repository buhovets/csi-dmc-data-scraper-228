import scrapy


class CsiItem(scrapy.Item):
    title = scrapy.Field()
    text = scrapy.Field()
    images = scrapy.Field()
