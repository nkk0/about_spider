import scrapy


class AboutItem(scrapy.Item):
    author = scrapy.Field()
    text = scrapy.Field()
