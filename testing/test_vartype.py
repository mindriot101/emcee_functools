import pytest
from emcee_functools import Fixed


def test_fixed_can_contain_a_value():
    f = Fixed(5)
    assert f.value == 5


def test_fixed_value_does_not_change():
    f = Fixed(5)
    with pytest.raises(ValueError) as err:
        f.value += 5


def test_fixed_value_does_not_change_at_class_level():
    f = Fixed(5)
    with pytest.raises(ValueError) as err:
        f += 5


def test_string_representation():
    f = Fixed(5)
    assert str(f) == '<Fixed value 5>'
