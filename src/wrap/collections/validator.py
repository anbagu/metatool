from pydantic import validate_call

from src.wrap.stack import MetaWrap


class MetaValidate(MetaWrap):
    array_wraps=[validate_call(validate_return=True)]