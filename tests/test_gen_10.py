from app.gen_10 import value_10


def test_value_10():
    assert value_10(2) == 2 * 8 + 8
    assert value_10(0) == 8
