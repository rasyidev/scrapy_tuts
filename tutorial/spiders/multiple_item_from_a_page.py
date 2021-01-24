import scrapy


class MultipleItemFromAPageSpider(scrapy.Spider):
    name = 'multiple_item_from_a_page'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('div.quote'):
         item = {
             'author': quote.css('span .author::text').extract_first(),
             'quote': quote.css('span.text::text').extract_first(),
             'tags': quote.css('a.tag::text').extract()
         }
         yield item
