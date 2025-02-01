
from src.domain.documents import UserDocument, ArticleDocument, PostDocument, RepositoryDocument


class TestDocuments:
    def test_user_document(self):
        user_document = UserDocument(first_name="tae-su", last_name="kang")
        assert user_document.first_name == "tae-su"
        assert user_document.last_name == "kang"
        assert user_document.full_name == "tae-su kang"

    def test_article_document_save(self):
        user = UserDocument(first_name="tae-su", last_name="kang")
        data = {
            "Title": "지금까지 이런 놈은 없었다",
            "Subtitle": "도약의 해",
            "Content": "하나씩, 확실하게",
        }
        instance = ArticleDocument(
            platform="medium", 
            content=data,
            link="https://medium.com/@keep_selves_real/sample-post-id",
            author_id=user.id,
            author_full_name=user.full_name
            )
        instance = instance.save()
        assert isinstance(instance, ArticleDocument)
        assert instance.author_full_name == "tae-su kang"

    def test_post_document_bulk_insert(self):
        user = user = UserDocument(first_name="tae-su", last_name="kang")
        posts = [
            PostDocument(platform="linkedin", content="This is my first posting!", author_id=user.id, author_full_name=user.full_name),
            PostDocument(platform="linkedin", content="This is my second posting!", author_id=user.id, author_full_name=user.full_name)
        ]
        PostDocument.bulk_insert(posts)

    def test_repository_document_save(self):
        user = UserDocument(first_name="tae-su", last_name="kang")
        repo_name = "sample_project"  
        tree = {
            "app/app.py": "def main():\n    print('Welcome to the Sample Project!')",
            "app/helpers.py": "def subtract(a, b): return a - b",
            "docs/overview.md": "# Sample Project Overview\nThis document explains the project structure.",
            "requirements.txt": "flask\nnumpy\npandas",
        }
        instance = RepositoryDocument(
            platform="github",
            name=repo_name, 
            content=tree,
            link="https://github.com/keepselvesreal/Vault/Projects/sample",
            author_id=user.id,
            author_full_name=user.full_name
            )
        instance = instance.save()
        assert isinstance(instance, RepositoryDocument)
        assert isinstance(instance.content, dict)
        assert instance.name == repo_name
        assert instance.author_full_name == "tae-su kang"

    def test_article_document_save_with_same_user(self, same_user):
        data = {
            "Title": "지금까지 이런 놈은 없었다",
            "Subtitle": "도약의 해",
            "Content": "드디어 싹을 띄우다!",
        }
        instance = ArticleDocument(
            platform="medium", 
            content=data,
            link="https://medium.com/@keep_selves_real/sample-post-id",
            author_id=same_user.id,
            author_full_name=same_user.full_name
            )
        instance = instance.save()
        assert isinstance(instance, ArticleDocument)
        assert instance.author_full_name == "tae-su kang"

    def test_post_document_save_with_same_user(self, same_user):
        instance = PostDocument(
            platform="linkedin", 
            content={"temp": "This is my n번째 posting!"}, 
            author_id=same_user.id, 
            author_full_name=same_user.full_name
        )
        instance.save()
        assert isinstance(instance, PostDocument)
        assert isinstance(instance.content, dict)
        assert instance.platform == "linkedin"
        assert instance.author_full_name == "tae-su kang"

    def test_repository_document_save_with_same_user(self, same_user):
        repo_name = "sample_project2"  
        tree = {
            "app/app.py": "def main():\n    print('Welcome to the Sample Project!')",
            "app/helpers.py": "def subtract(a, b): return a - b",
            "docs/overview.md": "# Sample Project Overview\nThis document explains the project structure.",
            "requirements.txt": "flask\nnumpy\npandas",
        }
        instance = RepositoryDocument(
            platform="github",
            name=repo_name, 
            content=tree,
            link="https://github.com/keepselvesreal/Vault/Projects/sample2",
            author_id=same_user.id,
            author_full_name=same_user.full_name
            )
        instance = instance.save()
        assert isinstance(instance, RepositoryDocument)
        assert isinstance(instance.content, dict)
        assert instance.name == repo_name
        assert instance.author_full_name == "tae-su kang"


    