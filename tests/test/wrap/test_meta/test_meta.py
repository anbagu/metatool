import logging

import pytest
from pydantic import ValidationError

from src.metatool_anbagu.wrap.meta.meta import MetaLoggerValidator


@pytest.fixture(scope="function")
def dummy_string():
    class DummyString(metaclass=MetaLoggerValidator):
        def concat(self, a: str, b: str) -> str:
            return a + b

    yield DummyString()


@pytest.fixture(scope="function")
def misdef_dummy_string():
    class DummyString(metaclass=MetaLoggerValidator):
        def concat(self, a: str, b: str) -> int:
            return a + b

    yield DummyString()


class TestMetaValidator(): ...


class TestMetaLogger(): ...


class TestMetaLoggerValidator():
    def test_meta_logger_validator_ok(self, dummy_string):
        assert dummy_string.concat(a="Hello", b="World") == "HelloWorld"

    def test_meta_logger_validator_inp_err(self, dummy_string):
        with pytest.raises(ValidationError):
            dummy_string.concat(a="hello", b=1)

    def test_meta_logger_validator_out_err(self, misdef_dummy_string):
        with pytest.raises(ValidationError):
            misdef_dummy_string.concat(a="hello", b="")

    def test_meta_logger_validator_timer(self, caplog, dummy_string):
        logging.getLogger(dummy_string.concat.__module__).setLevel(logging.DEBUG)
        dummy_string.concat(a="Hello", b="World")
        assert "Calling" in caplog.text and "Finished" in caplog.text
