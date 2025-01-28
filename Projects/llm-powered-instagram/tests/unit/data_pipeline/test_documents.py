
from src.domain.documents import UserDocument


class TestDocuments:
    def test_user_document(self):
        user_document = UserDocument(first_name="tae-su", last_name="kang")
        assert user_document.first_name == "tae-su"
        assert user_document.last_name == "kang"
        assert user_document.full_name == "tae-su kang"
    