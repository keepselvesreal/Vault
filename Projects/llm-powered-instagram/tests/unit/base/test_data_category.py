from src.domain.types import DataCategory

class TestDataCategory:
    def test_data_category(self):
        posts_category = DataCategory.POSTS

        assert isinstance(posts_category, str)
        assert posts_category == "posts" 
