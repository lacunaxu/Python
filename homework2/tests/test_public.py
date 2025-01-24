import pytest
from lab2 import format_date, check_palindrome_tuples, join_by_delimiter


@pytest.mark.parametrize(
    "day, month, year, result",
    [
        (1, 8, 2000, "01 August, 2000"),
        (27, 1, 2003, "27 January, 2003"),
    ],
)
@pytest.mark.timeout(0.3)
def test_format_date_valid(day, month, year, result):
    assert format_date(day, month, year) == result


@pytest.mark.parametrize(
    "day, month, year",
    [
        (32, 1, 2003),
        (30, 13, 2003),
        (29, 2, 2003),
    ],
)
@pytest.mark.timeout(0.3)
def test_format_date_invalid(day, month, year):
    with pytest.raises(Exception, match=f"The given date: {day}, {month}, {year} is invalid"):
        format_date(day, month, year)


@pytest.mark.parametrize(
    "tups, result",
    [
        ([("abc", "cba"), ("madam", "madam")], True),
        ([("abc", "def"), ("ghi", "ihg")], False),
        ([("python", "nohtyp"), ("java", "avaj"), ("abc", "xyz")], False),
    ],
)
@pytest.mark.timeout(0.3)
def test_check_palindrome_tuples(tups, result):
    assert check_palindrome_tuples(tups) == result


@pytest.mark.parametrize(
    "tups",
    [
        ([(123, "321")]),
        ("abc, cba"),
        ([("abc", "cba", "extra")]),
        ([("", "cba")]),
    ],
)
@pytest.mark.timeout(0.3)
def test_check_palindrome_tuples_invalid_input(tups):
    with pytest.raises(Exception) as excinfo:
        check_palindrome_tuples(tups)
    assert str(excinfo.value) == "Invalid Input"


@pytest.mark.parametrize(
    "substrings, delimiter, result",
    [
        (["this", "is", "DSCI", "510"], " ", "this is DSCI 510"),
        (["I", "am", "a", "student"], ",", "I,am,a,student"),
        (
            ["this class", "is really nice!"],
            ",",
            "this class,is really nice!",
        ),
        ([], ",", ""),
        (["this", "class", "is", "nice!"], "", "thisclassisnice!"),
    ],
)
@pytest.mark.timeout(0.3)
def test_join_by_delimiter_valid(substrings, delimiter, result):
    assert join_by_delimiter(substrings, delimiter) == result


@pytest.mark.parametrize(
    "substrings, delimiter",
    [
        ("not a list", ","),
        (["wrong", "delimiter"], 5),
        ([3, 4, 5], ","),
    ],
)
@pytest.mark.timeout(0.3)
def test_join_by_delimiter_invalid(substrings, delimiter):
    with pytest.raises(Exception, match="Invalid Input"):
        join_by_delimiter(substrings, delimiter)
