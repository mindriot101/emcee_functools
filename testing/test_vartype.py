import pytest
from emcee_functools import Fixed


@pytest.fixture
def fixed():
    return Fixed(5)


def test_fixed_can_contain_a_value(fixed):
    assert fixed.value == 5


def test_fixed_value_does_not_change(fixed):
    with pytest.raises(ValueError) as err:
        fixed.value += 5


def test_fixed_value_does_not_change_at_class_level(fixed):
    with pytest.raises(ValueError) as err:
        fixed += 5


def test_string_representation(fixed):
    assert str(fixed) == '<Fixed value 5>'
