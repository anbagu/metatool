import pytest

from src.metatool_anbagu.wrap.stack import WrapStackPreparer

@pytest.fixture(scope="function")
def array_of_stack():
    yield [lambda x: lambda *_,**__:x()+1]

@pytest.fixture(scope="function")
def wsp(array_of_stack):
    yield WrapStackPreparer(array_of_stack)

class TestWrapStackPreparer:
    def test_wrap_stack_preparer(self, wsp, array_of_stack):
        assert wsp.array_wraps == array_of_stack

    def test_set_item(self, wsp):
        def c():
            return 1

        wsp["c"]=c
        assert wsp["c"]()== 2





