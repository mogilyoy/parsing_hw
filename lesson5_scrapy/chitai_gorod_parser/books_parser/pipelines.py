# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient




class BooksParserPipeline:
    def __init__(self):
        client = MongoClient()
        self.mongo_db = client.chitai_gorod
        pass


    def process_item(self, item, spider):

        item = self.clear_item(item)
        python_books = self.mongo_db[spider.name]
        python_books.insert_one(item)
        
        return item 
    

    def clear_item(self, item):
        if item['author']:
            item['author'] = item['author'].strip().replace('\n', '')

        if item['book_id']:
            item['book_id'] = item['book_id'].strip().replace('\n', '')

        if item['name']:
            item['name'] = item['name'].strip().replace('\n', '')

        if item['price']:
            item['price'] = item['price'].strip().replace('\n', '').replace('\\xa0', '')

        if item['year']:
            item['year'] = item['year'].strip().replace('\n', '')

        return item
        
    
