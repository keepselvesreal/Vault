

from src.application.crawlers.dispatcher import CrawlerDispatcher
from src.domain.documents import UserDocument

class  TestCrawler:
    def test_instagram_crawler(self):
        crawl_dispatcher = CrawlerDispatcher.build().register_instagram()
        insta_crawler = crawl_dispatcher.get_crawler(url="https://www.instagram.com")
        user = UserDocument(first_name="tae-su", last_name="kang")
        insta_crawler.extract(link="https://wwww.instagram/go-getter", user=user)