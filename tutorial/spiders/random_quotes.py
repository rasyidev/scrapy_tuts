import scrapy


class RandomQuotesSpider(scrapy.Spider):
    name = 'random_quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/random']

    def parse(self, response):
        yield {
            'author': response.css('span .author::text').get(),
            'quotes': response.css('span.text::text').get(),
            'tags': response.css('.tag::text').getall()
        }
