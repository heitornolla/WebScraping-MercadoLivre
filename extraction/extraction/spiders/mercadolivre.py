import scrapy

class MercadoLivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/baixo-5-cordas"]

    def parse(self, response):
        products = response.css('div.ui-search-result__wrapper')

        for product in products:
            prices = product.css('span.andes-money-amount__fraction::text').getall()

            yield {
                'name': product.css('a.poly-component__title::text').get(),
                'seller': product.css('span.poly-component__seller::text').get(),
                'old_price':prices[0] if len (prices) > 0 else None, 
                'new_price':prices[1] if len (prices) > 1 else None, 
                'reviews_rating_number': product.css('span.poly-reviews__rating::text').get(),
                'reviews_amount': product.css('span.poly-reviews__total::text').get()
            }
        pass
