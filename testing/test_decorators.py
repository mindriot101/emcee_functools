from emcee_functools import func_signature, Fixed, Varying


def test_parameter_manipulation():
    @func_signature(a=Fixed(), b=Varying())
    def test_fn(**params):
        return params
