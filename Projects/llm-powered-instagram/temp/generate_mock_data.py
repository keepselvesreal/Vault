import os
import sys
from uuid import uuid4
from random import choice, randint

from src.application.utils import split_user_full_name
from src.domain.documents import UserDocument, RepositoryDocument, PostDocument, ArticleDocument

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# 사용자 3명 생성
users = [
    UserDocument(id=uuid4(), first_name="Alice", last_name="Johnson"),
    UserDocument(id=uuid4(), first_name="Bob", last_name="Smith"),
    UserDocument(id=uuid4(), first_name="Charlie", last_name="Brown"),
]

# 가상 데이터 생성 함수
def generate_mock_data():
    repo_names = ["project-alpha", "repo-beta", "gamma-lib", "delta-framework", "epsilon-tool"]
    user_full_names = ["Alice Johnson", "Bob Smith", "Charlie Brown"]
    for user_full_name in user_full_names:
        first_name, last_name = user_full_name.split()
        user = UserDocument.get_or_create(first_name=first_name, last_name=last_name)
        # RepositoryDocument 데이터 생성
        for _ in range(10):
            repo_name = choice(repo_names) + f"-{randint(1,100)}"
            repo = RepositoryDocument(
                content={"README.md": "# Sample Content"},
                platform="github",
                author_id=user.id,
                author_full_name=user.full_name,
                name=repo_name,
                link=f"https://github.com/{user.first_name.lower()}/{repo_name}"
            )
            repo.save()
        
        # PostDocument 데이터 생성
        for _ in range(10):
            post = PostDocument(
                content={"text": "Sample LinkedIn Post Content"},
                platform="linkedin",
                author_id=user.id,
                author_full_name=user.full_name,
                image=None,
                link=f"https://www.linkedin.com/in/{user.first_name.lower()}-{randint(100,999)}"
            )
            post.save()
        
        # ArticleDocument 데이터 생성
        for _ in range(10):
            article = ArticleDocument(
                content={"title": "Sample Medium Article", "body": "Lorem ipsum dolor sit amet."},
                platform="medium",
                author_id=user.id,
                author_full_name=user.full_name,
                link=f"https://medium.com/@{user.first_name.lower()}/article-{randint(1000,9999)}"
            )
            article.save()

generate_mock_data()

