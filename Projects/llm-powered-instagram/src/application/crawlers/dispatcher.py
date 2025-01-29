import re
from urllib.parse import urlparse

from loguru import logger

from .base import BaseCrawler
from .instagram import InstagramCrawler
from .custom_article import CustomArticleCrawler

class CrawlerDispatcher:
    def __init__(self) -> None:
        self._crawlers = {}

    @classmethod
    def build(cls) -> "CrawlerDispatcher":
        dispatcher = cls()

        return dispatcher
    
    def register(self, domain: str, crawler: type[BaseCrawler]) -> None:
        parsed_domain = urlparse(domain)
        domain = parsed_domain.netloc
        
        self._crawlers[r"https://(www\.)?{}*".format(re.escape(domain))] = crawler
    
    def register_instagram(self) -> "CrawlerDispatcher":
        self.register("https://www.instagram.com", InstagramCrawler)

        return self

    def get_crawler(self, url: str) -> BaseCrawler:
        for pattern, crawler in self._crawlers.items():
            if re.match(pattern, url):
                return crawler()
            
        logger.warning(f"No crawler found for {url}. Defaulting to CustomArticleCrawler")

        return CustomArticleCrawler()

