import scrapy

class quotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["'http://quotes.toscrape.com/"]
    start_urls = [ # Треба взяти лише ось ці дві сторінки.
        "http://quotes.toscrape.com/page/1/",
        "http://quotes.toscrape.com/page/2/",
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
            }
