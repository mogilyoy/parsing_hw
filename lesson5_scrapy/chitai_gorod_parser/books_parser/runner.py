from twisted.internet import reactor

from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from spiders.python_books import PythonBooksSpider


if __name__ == '__main__':
    # Have some problems with settings. For whatever reason the get_project_settings doesn't work properly. 
    # configure_logging()
    settings = get_project_settings()

    # runner = CrawlerRunner(settings)
    # runner.crawl(PythonBooksSpider)

    # reactor.run()