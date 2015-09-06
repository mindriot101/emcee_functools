from collections import OrderedDict


class Fixed(object):
    '''
    Class describing a parameter which does not vary
    '''

    def __init__(self, value=None):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, *args, **kwargs):
        raise ValueError("Fixed values cannot change")

    def __add__(self, other):
        raise ValueError("Fixed values cannot change")

    def __str__(self):
        return '<Fixed value {value}>'.format(value=self.value)


class Varying(object):
    '''
    Placeholder for varying parameter
    '''


def func_signature(**param_mapping):
    '''
    '''

    def decorator(fn):

        varying, fixed = [], []
        for key in param_mapping:
            value = param_mapping[key]
            if isinstance(value, Fixed):
                fixed.append(key)
            else:
                varying.append(key)

        varying.sort()
        fixed.sort()

        fn_args = ', '.join(fixed)
        fn_code = 'def inner(p, {0}):\n'.format(fn_args)
        fn_code += '    return fn('
        args_entries = [
            '{name}=p[{i}]'.format(name=arg,
                                   i=i) for (i, arg) in enumerate(varying)
        ]
        kwargs_entries = ['{name}={name}'.format(name=arg) for arg in fixed]
        fn_code += ', '.join(args_entries + kwargs_entries) + ')'

        exec(fn_code, locals(), globals())

        return inner

    return decorator
