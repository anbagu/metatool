from src.wrap.decorators.logger import logged
from src.wrap.decorators.validator import validate_call_and_return
from src.wrap.stack import MetaWrap


class MetaValidator(MetaWrap):
    __array_wraps__ = [validate_call_and_return]


class MetaLogger(MetaWrap):
    __array_wraps__ = [logged]


class MetaLoggerValidator(MetaLogger, MetaValidator): ...
