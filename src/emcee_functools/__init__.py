class Fixed(object):
    '''
    Class describing a parameter which does not vary
    '''

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, *args, **kwargs):
        raise ValueError("Fixed values cannot change")
