from app.gen_19 import value_19


def test_value_19():
    assert value_19(2) == 2 * 4 + 1
    assert value_19(0) == 1
