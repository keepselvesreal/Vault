from typing_extensions import Annotated

from zenml import get_step_context, step

from src.domain.documents import UserDocument
from src.application.utils.split_user_full_name import split_user_full_name

@step
def get_or_create_user(user_full_name: str) -> Annotated[UserDocument, "user"]:
    first_name, last_name = split_user_full_name(user_full_name)

    user = UserDocument.get_or_create(first_name=first_name, last_name=last_name)

    step_context = get_step_context()
    step_context.add_output_metadata(output_name="user", metadata=_get_metadata(user_full_name, user))
    
    return user


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