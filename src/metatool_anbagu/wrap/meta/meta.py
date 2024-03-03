from src.metatool_anbagu.wrap.decorators.logger import logged
from src.metatool_anbagu.wrap.decorators.validator import validate_call_and_return
from src.metatool_anbagu.wrap.stack import MetaWrap


class MetaValidator(MetaWrap):
    __array_wraps__ = [validate_call_and_return]


class MetaLogger(MetaWrap):
    __array_wraps__ = [logged]


class MetaLoggerValidator(MetaLogger, MetaValidator): ...
