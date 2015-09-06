import inspect
from emcee_functools import func_signature, Fixed, Varying


@func_signature(a=Fixed(), b=Varying())
def fn(**params):
    return params['a'], params['b']


def test_parameter_manipulation():
    sig = inspect.signature(fn)
    assert 'p' in sig.parameters


def test_values():
    a_input = 1
    b_input = 15
    p = [a_input,]

    a_result, b_result = fn(p, b=b_input)
    assert a_result == a_input and b_result == b_input
