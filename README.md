# I use this repo while learning Scrapy

### Create Spider via CLI
> scrapy genspider <spidername> <website_url>
example:
> scrapy genspider quotes toscrape.com

### Run Spider via CLI
> scrapy runspider /path/to/spider/spider.py
or
> scrapu crawl <spider_name>

### Export data to json via CLI
> scrapy crawl <spider_name> -o <output_filename>