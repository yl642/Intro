# test_file1.py
import pytest


@pytest.mark.parametrize('a, b, output, expected,', [
    (0.5, 0.2, 0.3, True),
    (2, 3, 5, False),
    ('a', 5, False, True),
    (2, True, False, True),
])
def test_sub(a, b, output, expected):
    from file1 import sub
    answer = sub(a, b) == output
    assert answer == expected


@pytest.mark.parametrize('x, output, expected,', [
    # output should be 2carried out as tuples
    ([6, 1, 5, 2, 10, 3, 4], (1, 10), True),
    ([6, 1, 5, 2, True, 10, 3, 4], False, True),
    ([6, 1, 5, 2, 'a', 10, 3, 4], False, True),
    ([61, 1, 15, 2, 100, 10, 3, 4], (100, 1), False),
])
def test_min_max(x, output, expected):
    from file1 import min_max
    answer = min_max(x) == output
    assert answer == expected
