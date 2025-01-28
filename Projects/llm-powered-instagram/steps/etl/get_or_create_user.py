from typing_extensions import Annotated

from src.domain.documents import UserDocument

def get_or_create_user(user_full_name: str) -> Annotated[UserDocument, "user"]:
    first_name, last_name =


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