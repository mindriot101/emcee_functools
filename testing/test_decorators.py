import inspect
from emcee_functools import func_signature, Fixed, Varying


def test_parameter_manipulation():
    @func_signature(a=Fixed(), b=Varying())
    def test_fn(**params):
        pass

    sig = inspect.signature(test_fn)
    assert 'p' in sig.parameters
