class WrapStackPreparer(dict):

    def __init__(self, array_wraps):
        super().__init__()
        self.array_wraps = array_wraps

    def __setitem__(self, key, value):
        if callable(value):
            for wrap in self.array_wraps:
                value = wrap(value)
        dict.__setitem__(self, key, value)


class MetaBase(type):
    array_wraps = None
    def __add__(self, other):
        array_wraps = self.array_wraps + other.array_wraps
        merged = super(self).__init__()
        merged.array_wraps = array_wraps
        return merged

# !todo wrap only stacks decorators decorator stack is defined on collections as an StackableWrapper class that allows sum()
# !todo then add other meta tools
# The metaclass
class MetaWrap(MetaBase):

    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        array_wraps = kwargs.get('array_wraps', metacls.array_wraps) or []
        return WrapStackPreparer(array_wraps)

    def __new__(metacls, name, bases, classdict, **kwargs):
        result = type.__new__(metacls, name, bases, classdict)
        return result
