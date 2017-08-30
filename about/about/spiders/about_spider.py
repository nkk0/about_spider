from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from about.items import AboutItem


class AboutSpider(CrawlSpider):
    name = 'about'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    rules = (
        Rule(LinkExtractor(allow='quotes.toscrape.com/author'), callback='parse_item'),
        Rule(LinkExtractor(allow='quotes.toscrape.com/page'), follow=True)
    )

    def parse_item(self, response):
        self.log('Scraping: ' + response.url)

        item = AboutItem()
        item['author'] = response.css('.author-title')[0].css('::text').extract()[0].strip()
        item['text'] = response.css('.author-description')[0].css('::text').extract()[0].strip()

        yield item
