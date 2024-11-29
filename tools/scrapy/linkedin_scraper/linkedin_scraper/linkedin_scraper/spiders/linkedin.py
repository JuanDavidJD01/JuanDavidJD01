import scrapy


class LinkedinSpider(scrapy.Spider):
    name = "wikipedia"
    allowed_domains = ["es.wikipedia.org"]
    start_urls = ["https://es.wikipedia.org/wiki/Scrapy"]

    def parse(self, response):
        filename = f"page-{response.url.split('/')[-1]}.html"
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
