import pytest

from src.application.utils.split_user_full_name import split_user_full_name


def test_split_user_full_name():
    # 정상적인 이름 입력
    assert split_user_full_name("Tae-su Kang") == ("Tae-su", "Kang")
    assert split_user_full_name("John Doe") == ("John", "Doe")
    assert split_user_full_name("Alice") == ("Alice", "Alice")  # 이름 하나만 있을 경우

    # 여러 단어로 구성된 이름
    assert split_user_full_name("Jean Claude Van Damme") == ("Jean Claude Van", "Damme")
    
    # 공백만 있는 경우
    with pytest.raises(Exception):
        split_user_full_name(" ")

    # # 빈 문자열
    # with pytest.raises(Exception):
    #     split_user_full_name("")

    # None 입력
    with pytest.raises(Exception):
        split_user_full_name(None)