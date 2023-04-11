import scrapy


class CategorySpider(scrapy.Spider):
    name = 'category'

    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.start_urls = kwargs.get('start_url').split(',') or ['https://krasn.russcvet.ru/catalog/enamels/'] 


    def parse(self, response, **kwargs):
        # парсинг товаров на странице
        for item in response.css('div.catalog-item'):
            name = item.css('div.name a::text').extract_first()
            price = item.css('div.price span.catalog-item-price::text').extract_first()
            
            yield {'Name': name, 'Price': price}

        # поиск ссылки на следующую страницу
        next_page = response.css('a.modern-page-next::attr("href")').extract_first()

        # переход на следующую страницу
        if next_page:
            yield response.follow(next_page, callback=self.parse)



    
        
        