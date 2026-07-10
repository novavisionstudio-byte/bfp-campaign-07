from app.gen_29 import value_29


def test_value_29():
    assert value_29(2) == 2 * 4 + 5
    assert value_29(0) == 5
