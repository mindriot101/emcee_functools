from emcee_functools import Fixed


def test_fixed_can_contain_a_value():
    f = Fixed(5)
    assert f.value == 5
