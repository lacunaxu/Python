from lab2 import format_date, check_palindrome_tuples, join_by_delimiter

def test_format_date():
    """
    Test the format_date function with valid and invalid inputs.
    """
    # Valid cases
    print(format_date(1, 8, 2000))  # Expected: "01 August, 2000"
    print(format_date(27, 1, 2003))  # Expected: "27 January, 2003"

    # Invalid cases
    invalid_dates = [(32, 1, 2003), (30, 13, 2003), (29, 2, 2003)]
    for day, month, year in invalid_dates:
        try:
            print(format_date(day, month, year))
        except Exception as e:
            print(e)  # Expected: Exception message indicating invalid date

def test_check_palindrome_tuples():
    """
    Test the check_palindrome_tuples function with valid and invalid inputs.
    """
    # Valid cases
    print(check_palindrome_tuples([("abc", "cba"), ("madam", "madam")]))  # Expected: True
    print(check_palindrome_tuples([("abc", "def"), ("ghi", "ihg")]))  # Expected: False

    # Invalid cases
    invalid_inputs = [
        [(123, "321")],
        "abc, cba",
        [("abc", "cba", "extra")],
        [("", "cba")],
    ]
    for invalid_input in invalid_inputs:
        try:
            print(check_palindrome_tuples(invalid_input))
        except Exception as e:
            print(e)  # Expected: Exception message indicating invalid input

def test_join_by_delimiter():
    """
    Test the join_by_delimiter function with valid and invalid inputs.
    """
    # Valid cases
    print(join_by_delimiter(["this", "is", "DSCI", "510"], " "))  # Expected: "this is DSCI 510"
    print(join_by_delimiter(["I", "am", "a", "student"], ","))  # Expected: "I,am,a,student"
    print(join_by_delimiter([], ","))  # Expected: ""
    print(join_by_delimiter(["this", "class", "is", "nice!"], ""))  # Expected: "thisclassisnice!"

    # Invalid cases
    invalid_cases = [
        ("not a list", ","),
        (["wrong", "delimiter"], 5),
        ([3, 4, 5], ","),
    ]
    for substrings, delimiter in invalid_cases:
        try:
            print(join_by_delimiter(substrings, delimiter))
        except Exception as e:
            print(e)  # Expected: Exception message indicating invalid input

# Call the test functions to execute the tests
test_format_date()
test_check_palindrome_tuples()
test_join_by_delimiter()
