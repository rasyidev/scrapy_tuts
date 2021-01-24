import scrapy


class FollowPaginationSpider(scrapy.Spider):
    name = 'follow_pagination'
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
         
         # follow pagination link
         next_page_url = response.css('li.next > a::attr(href)').extract_first()
         if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

