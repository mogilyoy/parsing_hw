import scrapy
from books_parser.items import BooksParserItem

class PythonBooksSpider(scrapy.Spider):
    name = "python_books"
    allowed_domains = ["chitai-gorod.ru"]
    start_urls = ["https://www.chitai-gorod.ru/search?phrase=python&page=1"]
    base_url = 'https://www.chitai-gorod.ru'

    def parse(self, response):
        pages_list = response.xpath("//span[@class='pagination__text']/text()")
        last_page = int(str(pages_list[-1].root.replace('\n', '').strip()))

        for i in range(1, last_page):
            yield response.follow(f'https://www.chitai-gorod.ru/search?phrase=python&page={i+1}', callback=self.parse)
        
        books_urls = response.xpath("//a[@class='product-card__picture product-card__row']/@href").getall()

        for url in books_urls:
            
            yield response.follow(self.base_url + url, callback=self.get_book_info)

    def get_book_info(self, response):
        
        name = response.xpath("//img[@class='product-gallery__image']/@alt").get()
        author = response.xpath("//a[@class='product-detail-title__author']/text()").get()
        year = response.xpath("//span[@itemprop='datePublished']/text()").get()
        price = response.xpath("//span[@itemprop='price']/text()").get()
        book_id = response.xpath("//div[@class='product-detail-characteristics']/div[1]/span[2]/text()").get()
        url = response.url
                
        yield BooksParserItem(
            name=name,
            author=author,
            year=year,
            price=price,
            book_id=book_id,
            url=url
        )


