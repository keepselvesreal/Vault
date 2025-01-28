

def split_user_full_name(user: str | None) -> tuple[str, str]:
    if user is None:
        raise Exception("User cannot be None") 

    name_tokens = user.split(" ")
    if len(name_tokens) == 0:
        raise Exception("User name cannot be empty or just whitespace")
    elif len(name_tokens) == 1:
        first_name, last_name = name_tokens[0], name_tokens[0]
    else:
        first_name, last_name = " ".join(name_tokens[:-1]), name_tokens[-1]
    return first_name, last_name