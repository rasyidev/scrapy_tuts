import scrapy


class LoginSpiderSpider(scrapy.Spider):
    name = 'login_spider'
    # allowed_domains = ['http://quotes.toscrape.com/login']
    login_url = 'http://quotes.toscrape.com/login'
    start_urls = [login_url]

    def parse(self, response):
        # extract the csrf_token
        token = response.css('input[name="csrf_token"]::attr(value)').extract_first()

        # create a dict with the form value
        data = {
            'csrf_token': token,
            'username': "123",
            'password': "123",
        }

        yield scrapy.FormRequest(url=self.login_url, formdata=data, callback=self.parse_quotes)

    def parse_quotes(self, response):
        # parse the main page after the spider is logged in
        for quote in response.css('div.quote'):
            yield {
                'author_name': quote.css('small.author::text').extract_first(),
                'author_url': quote.css('span a[href*="goodreads.com"]').extract_first()
            }