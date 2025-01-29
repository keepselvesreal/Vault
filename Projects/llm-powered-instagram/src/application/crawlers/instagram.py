import uuid

from .base import BaseCrawler
from src.domain.documents import PostDocument


class InstagramCrawler(BaseCrawler):
    model = PostDocument

    def extract(self, link: str, **kwargs) -> None:
        dummy_content = "dummy_content"
        dummy_content = {"main_content": "hi",
                         "comments": {"euna": "sorry",
                                     "eun": "bad"}}
        insatnce = self.model(
            content=dummy_content,
            platform="instagram",
            # author_id="go-getter",
            author_id=str(uuid.uuid4()),
            author_full_name="tae-su kang"
            )
        insatnce.save()

