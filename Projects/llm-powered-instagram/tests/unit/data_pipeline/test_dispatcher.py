

from src.application.crawlers.dispatcher import CrawlerDispatcher
from src.application.crawlers.instagram import InstagramCrawler

class TestDispatcher:
    def test_build(self):
        assert isinstance(CrawlerDispatcher.build(), CrawlerDispatcher)

    def test_register(self):
        crawl_dispatcher = CrawlerDispatcher()
        crawl_dispatcher.register("https://www.instagram.com", InstagramCrawler)
        assert any('instagram' in key for key in crawl_dispatcher._crawlers.keys())
        assert any(value is InstagramCrawler for value in crawl_dispatcher._crawlers.values())

    def test_register_instagram(self):
        crawl_dispatcher = CrawlerDispatcher()
        crawl_dispatcher.register_instagram()
        assert any('instagram' in key for key in crawl_dispatcher._crawlers.keys())
        assert any(value is InstagramCrawler for value in crawl_dispatcher._crawlers.values())

    def test_get_crawler(self):
        crawl_dispatcher = CrawlerDispatcher.build().register_instagram()
        crawler = crawl_dispatcher.get_crawler(url="https://www.instagram.com")
        assert isinstance(crawler, InstagramCrawler)
        # assert crawler is InstagramCrawler

    

