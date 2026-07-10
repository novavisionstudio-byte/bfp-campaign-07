from app.gen_14 import value_14


def test_value_14():
    assert value_14(2) == 2 * 2 + 4
    assert value_14(0) == 4
