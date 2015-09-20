import inspect
from emcee_functools import func_signature, Fixed, Varying


def _fn(**params):
    return params


def test_parameter_manipulation():
    fn = func_signature(a=Varying(), b=Fixed())(_fn)
    sig = inspect.signature(fn)
    assert 'p' in sig.parameters


def test_values():
    fn = func_signature(a=Fixed(), b=Varying(), c=Varying())(_fn)
    assert fn([1, 2], a=3) == {'a': 3, 'b': 1, 'c': 2,}
