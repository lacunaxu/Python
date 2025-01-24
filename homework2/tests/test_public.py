from typing import List, Tuple

def format_date(day: int, month: int, year: int) -> str:
    """
    Format a given date into the format "DD Month, YYYY".

    Args:
        day (int): The day of the month.
        month (int): The month of the year (1-12).
        year (int): The year.

    Returns:
        str: The formatted date as "DD Month, YYYY".

    Raises:
        Exception: If the provided date is invalid.
    """
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    if month < 1 or month > 12:
        raise Exception(f"The given date: {day}, {month}, {year} is invalid")

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[1] = 29  # Leap year

    if day < 1 or day > days_in_month[month - 1]:
        raise Exception(f"The given date: {day}, {month}, {year} is invalid")

    return f"{day:02d} {months[month - 1]}, {year}"

def check_palindrome_tuples(tups: List[Tuple[str, str]]) -> bool:
    """
    Check if all pairs of strings in the list are palindromes of each other.

    Args:
        tups (List[Tuple[str, str]]): A list of string pairs.

    Returns:
        bool: True if all pairs are palindromes of each other, otherwise False.

    Raises:
        Exception: If the input is invalid.
    """
    if not isinstance(tups, list) or not all(isinstance(pair, tuple) and len(pair) == 2 for pair in tups):
        raise Exception("Invalid Input")

    for s1, s2 in tups:
        if not isinstance(s1, str) or not isinstance(s2, str) or s1[::-1] != s2:
            return False

    return True

def join_by_delimiter(substrings: List[str], delimiter: str) -> str:
    """
    Join a list of strings with a specified delimiter.

    Args:
        substrings (List[str]): The list of strings to join.
        delimiter (str): The delimiter to use for joining the strings.

    Returns:
        str: The joined string.

    Raises:
        Exception: If the input is invalid.
    """
    if not isinstance(substrings, list) or not all(isinstance(sub, str) for sub in substrings):
        raise Exception("Invalid Input")

    if not isinstance(delimiter, str):
        raise Exception("Invalid Input")

    return delimiter.join(substrings)

# Example usage
if __name__ == "__main__":
    # Example for format_date
    try:
        print(format_date(1, 8, 2000))
        print(format_date(29, 2, 2020))  # Leap year
    except Exception as e:
        print(e)

    # Example for check_palindrome_tuples
    try:
        palindrome_tuples = [("abc", "cba"), ("madam", "madam")]
        print(check_palindrome_tuples(palindrome_tuples))  # True

        invalid_tuples = [("abc", "def"), ("ghi", "ihg")]
        print(check_palindrome_tuples(invalid_tuples))  # False
    except Exception as e:
        print(e)

    # Example for join_by_delimiter
    try:
        substrings = ["this", "is", "DSCI", "510"]
        print(join_by_delimiter(substrings, " "))  # "this is DSCI 510"
    except Exception as e:
        print(e)
