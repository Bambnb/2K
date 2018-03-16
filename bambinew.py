class BnbspiderSpider(scrapy.Spider):
    name = "bnbspider"
    allowed_domains = ["airbnb.com"]
    start_urls = (
        'https://www.airbnb.com/',
    )

    def parse(self, response):
        pass
