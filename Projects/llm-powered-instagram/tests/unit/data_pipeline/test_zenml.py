from zenml import get_step_context, step

from src.domain.documents import UserDocument


class TestZenML:
    def test_add_output_metatdata(self):

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
        user = UserDocument(first_name="tae-su", last_name="kang")
        
        @step
        def add_output_metadata():
            step_context = get_step_context()
            step_context.add_output_metadata(output_name="user", metadata= _get_metadata(user_full_name, user))
