from typing_extensions import Annotated

from zenml import step, get_step_context

from src.domain.documents import UserDocument
from steps.etl.get_or_create_user import get_or_create_user
from src.application.utils import split_user_full_name


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

    def test_get_or_create_user(self):
        # @step
        # def get_or_create_user(user_full_name: str) -> Annotated[UserDocument, "user"]:
        #     first_name, last_name = split_user_full_name(user_full_name)

        #     user = UserDocument.get_or_create(first_name=first_name, last_name=last_name)

        #     step_context = get_step_context()
        #     step_context.add_output_metadata(output_name="user", metadata=self._get_metadata(user_full_name, user))
            
        #     return user
        user_full_name = "tae-su kang"
        user = get_or_create_user(user_full_name)
        assert isinstance(user, UserDocument)
        assert user.first_name == "tae-su"
        assert user.last_name == "kang"
        assert user.Settings.name == "users"

    def _get_metadata(self, user_full_name: str, user: UserDocument) -> dict:
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

    
