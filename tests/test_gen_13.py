from app.gen_13 import value_13


def test_value_13():
    assert value_13(2) == 2 * 9 + 6
    assert value_13(0) == 6
