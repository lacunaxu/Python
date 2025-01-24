import pytest
from lab1 import simple_interest, uppercase_count, distance_between_points


@pytest.mark.parametrize(
    "principal, rate, years, result",
    [
        (1000, 5, 2, 100.0),
        (5, 5, 5, 1.25),
        (500, 20, 10, 1000.0),
    ],
)
@pytest.mark.timeout(0.3)
def test_simple_interest(principal, rate, years, result):
    assert pytest.approx(simple_interest(principal, rate, years), abs=1e-2) == result


@pytest.mark.parametrize(
    "s, result",
    [
        ("Data Science", 2),
        ("DATA", 4),
        ("DATA SCIence", 7),
    ],
)
@pytest.mark.timeout(0.3)
def test_uppercase_count(s, result):
    assert uppercase_count(s) == result


@pytest.mark.parametrize(
    "x1, y1, x2, y2, result",
    [
        (1, 1, 4, 5, 5.0),
        (2, 3, 5, 7, 5.0),
        (3, 4, 6, 8, 5.0),
    ],
)
@pytest.mark.timeout(0.3)
def test_distance_between_points(x1, y1, x2, y2, result):
    assert pytest.approx(distance_between_points(x1, y1, x2, y2), abs=1e-2) == result
