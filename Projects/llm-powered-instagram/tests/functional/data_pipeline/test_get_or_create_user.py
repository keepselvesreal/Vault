
from src.domain.documents import UserDocument


class TestGetOrCreateUser:
    def test_get_metadata(self):
        def _get_metadata(user_full_name: str, user: UserDocument) -> dict:
            return {
                "query": {
                    "user_full_name": user_full_name
                },
                "retrieved": {
                    "user_id": str(user.id),
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                }
            }
        user_full_name = "tae-su kang"
        test_user = UserDocument(first_name="tae-su", last_name="kang")
        result = _get_metadata(user_full_name, test_user)
        
        assert result["query"]["user_full_name"] == "tae-su kang" 
        assert "user_id" in result["retrieved"]
    
