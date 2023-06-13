import pytest

from word_wrap.warp import wrap_yngwie, wrap_recursive, wrap_tail_recursive, wrap_loop

wrap_implementations = [wrap_yngwie, wrap_recursive, wrap_tail_recursive, wrap_loop]


@pytest.mark.parametrize("function", wrap_implementations)
def test_wrap_empty_string(function):
    assert function('', 0) == ''
