from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from hackernews_scrapy.items import HackerNewsItem


class AboutSpider(CrawlSpider):
    name = 'about'
    allowed_domains = ['http://quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/']

    rules = (
        Rule(LinkExtractor(allow='http://quotes.toscrape.com/author'), callback='parse_item', follow=True)
    )
