import pytest
from lab3 import compute_persistence, is_digit_power_sum, is_valid_product_code


@pytest.mark.parametrize(
    "num, result",
    [
        (39, 3),
        (999, 4),
        (4, 0),
    ],
)
@pytest.mark.timeout(0.3)
def test_compute_persistence_valid(num, result):
    assert compute_persistence(num) == result


@pytest.mark.parametrize(
    "num",
    [(-5), ("hello")],
)
@pytest.mark.timeout(0.3)
def test_compute_persistence_invalid(num):
    with pytest.raises(Exception, match="Invalid input"):
        compute_persistence(num)


@pytest.mark.parametrize(
    "num, power, result",
    [
        (153, 3, True),
        (9474, 4, True),
        (12, 3, False),
    ],
)
@pytest.mark.timeout(0.3)
def test_is_digit_power_sum_valid(num, power, result):
    assert is_digit_power_sum(num, power) == result


@pytest.mark.parametrize(
    "num, power",
    [(-18, 2), (1234, "three")],
)
@pytest.mark.timeout(0.3)
def test_is_digit_power_sum_invalid(num, power):
    with pytest.raises(Exception, match="Invalid input"):
        is_digit_power_sum(num, power)


@pytest.mark.parametrize(
    "code, result",
    [
        ("A1B-3456CDEF", True),
        ("AbCD1234567-", False),
        ("a1-Bc2DEf34g", True),
        ("A1Bc2DeF34", False),
        ("ABCDE12-FGHI", False),
        ("&A907y_Chj-FGHI", False),
    ],
)
@pytest.mark.timeout(0.3)
def test_is_valid_product_code(code, result):
    assert is_valid_product_code(code) == result
