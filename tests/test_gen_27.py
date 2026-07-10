from app.gen_27 import value_27


def test_value_27():
    assert value_27(2) == 2 * 3 + 6
    assert value_27(0) == 6
