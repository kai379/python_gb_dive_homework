import pytest
from Users import Users, Company


@pytest.fixture
def user_1():
    return Users('Толя', '758', '5')


@pytest.fixture
def user_2():
    return Users('Вобла', '59', '6')


@pytest.fixture
def user_3():
    return Users('Вобла', '59', '6')


def test_eq(user_2, user_3):
    assert user_2 == user_3


def test_hash(user_2, user_3):
    assert hash(user_2) == hash(user_3)


def test_repr(capfd, user_1):
    print(user_1)
    captured = capfd.readouterr()
    assert captured.out[:-1] == f'({user_1.name}, {user_1.user_id}, {user_1.user_lvl})'


if __name__ == '__main__':
    pytest.main(['-v'])
