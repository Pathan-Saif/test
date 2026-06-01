from solution import multiply


def test_positive_numbers():
    assert multiply(6, 7) == 42


def test_negative_number():
    assert multiply(-3, 9) == -27