class WrapStackPreparer(dict):

    def __init__(self, array_wraps=None):
        array_wraps = array_wraps or []
        super().__init__()
        self.array_wraps = array_wraps

    def __setitem__(self, key, value):
        if callable(value):
            for wrap in self.array_wraps:
                value = wrap(value)
        dict.__setitem__(self, key, value)


# !todo then add other meta tools
# The metaclass
class MetaWrap(type):
    __array_wraps__ = None

    def __init_subclass__(cls, **kwargs): ...

    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        metacls._init_array_wraps(**kwargs)
        metacls._inherit_array_wraps()
        return WrapStackPreparer(metacls.__array_wraps__)

    def __new__(metacls, name, bases, class_dict, **kwargs):
        result = super().__new__(metacls, name, bases, class_dict)
        return result

    @classmethod
    def _init_array_wraps(metacls, array_wraps=None):
        metacls.__array_wraps__ = array_wraps or []

    @classmethod
    def _inherit_array_wraps(metacls):
        for metabase in metacls.__bases__:
            if getattr(metabase, '__array_wraps__', None) is not None:
                metacls.__array_wraps__ += metabase.__array_wraps__
