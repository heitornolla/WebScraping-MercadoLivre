import os
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

save_path = os.path.join(os.getcwd(), 'data')

class MercadoLivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/baixo-5-cordas"]

    page_count = 1
    max_pages = 20


    def parse(self, response):
        products = response.css('div.ui-search-result__wrapper')

        for product in products:
            # Mercado Livre stores multiple "prices" in this single span
            prices = product.css('span.andes-money-amount__fraction::text').getall()

            yield {
                'name': product.css('a.poly-component__title::text').get(),
                'seller': product.css('span.poly-component__seller::text').get(),
                'price':prices[0] if len (prices) > 0 else None, 
                'reviews_rating_number': product.css('span.poly-reviews__rating::text').get(),
                'reviews_amount': product.css('span.poly-reviews__total::text').get()
            }

        if self.page_count < self.max_pages:
            next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
            if next_page:
                self.page_count += 1
                yield scrapy.Request(url=next_page, callback=self.parse)


    def run_spider():
        os.makedirs(save_path, exist_ok=True)
        process = CrawlerProcess(settings={
            **get_project_settings(),
            "FEEDS": {
                os.path.join(save_path, 'data.json'): {
                    "format": "json",
                    "overwrite": True,
                }
            }
        })
        process.crawl(MercadoLivreSpider)
        process.start()
