from tqdm import tqdm

from zenml import get_step_context

# from src.application.crawlers.dispatcher import CrawlerDispatcher

class TestCrawlLinks:
    def test_crawl_links(self, CrawlerDispatcher):
        dispatcher = CrawlerDispatcher.build().register_instagram()

        metadata = {}
        successfull_crawls = 0
        for link in tqdm(links):
            successfull_crawl, crawled_domain = _crawl_link(dispatcher, link, user)
            successfull_crawls += successfull_crawl

            metadata = _add_to_metadata(metadata, crawled_domain, successfull_crawl)

        step_context = get_step_context()
        step_context.add_output_metadata(output_name="crawled_links", metadata=metadata)

        return links # assert로 확인
    
    def test_crawl_link(dispatcher: CrawlerDispatcher, link: str, user: UserDocument) -> tuple[bool, str]:
        crawler = dispatcher.get_crawler(link)
        crawler_domain = urlparse(link).netloc

        try:
            crawler.extract(link=link, user=user)

            return (True, crawler_domain)
        except Exception as e:
            logger.error(f"An error occurred while crowling: {e!s}")

            return (False, crawler_domain)
        
    def test_add_to_metadata(metadata: dict, domain: str, successfull_crawl: bool) -> dict:
        pass


