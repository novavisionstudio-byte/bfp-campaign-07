from app.gen_31 import value_31


def test_value_31():
    assert value_31(2) == 2 * 9 + 7
    assert value_31(0) == 7
