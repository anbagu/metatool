class WrapStackPreparer(dict):

    def __init__(self, array_wraps):
        super().__init__()
        self.array_wraps = array_wraps

    def __setitem__(self, key, value):
        if callable(value):
            for wrap in self.array_wraps:
                value = wrap(value)
        dict.__setitem__(self, key, value)


# The metaclass
class MetaWrap(type):

    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        return WrapStackPreparer(**kwargs)

    def __new__(metacls, name, bases, classdict, **kwargs):
        result = type.__new__(metacls, name, bases, classdict)
        return result
