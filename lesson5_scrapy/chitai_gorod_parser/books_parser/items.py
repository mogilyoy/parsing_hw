# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksParserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    year = scrapy.Field()
    price = scrapy.Field()
    book_id = scrapy.Field()
    url = scrapy.Field()
    _id = scrapy.Field()

    
