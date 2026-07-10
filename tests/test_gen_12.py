from app.gen_12 import value_12


def test_value_12():
    assert value_12(2) == 2 * 4 + 8
    assert value_12(0) == 8
