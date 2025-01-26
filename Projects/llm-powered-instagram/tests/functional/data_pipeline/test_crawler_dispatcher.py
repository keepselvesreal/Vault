import pytest

class TestCrawlerDispatcher:
    @pytest.fixture
    def test_build(self, CrawlerDispatcher):
        dispatcher = CrawlerDispatcher.build()
        assert isinstance(dispatcher, CrawlerDispatcher)
    