from app.gen_30 import value_30


def test_value_30():
    assert value_30(2) == 2 * 6 + 4
    assert value_30(0) == 4
