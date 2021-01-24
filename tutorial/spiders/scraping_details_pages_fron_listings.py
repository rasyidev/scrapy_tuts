import scrapy


class ScrapingDetailsPagesFromListingsSpider(scrapy.Spider):
    name = 'scraping_details_pages_from_listings'
    # allowed_domains = ['http://quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # follow author details links
        urls = response.css('div.quote > span > a::attr(href)').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)

        # follow pagination links
        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_details(self, response):
        yield {
             'author': response.css('h3.author-title::text').extract_first(),
             'born_date': response.css('span.author-born-date::text').extract_first()
        }
