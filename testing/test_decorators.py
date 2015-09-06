import inspect
from emcee_functools import func_signature, Fixed, Varying


@func_signature(a=Fixed(), b=Varying(), c=Varying())
def fn(**params):
    return params


def test_parameter_manipulation():
    sig = inspect.signature(fn)
    assert 'p' in sig.parameters


def test_values():
    assert fn([1, 2], a=3) == {'a': 3, 'b': 1, 'c': 2,}
