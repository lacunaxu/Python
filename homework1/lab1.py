# Include your imports here
import math


def simple_interest(principal: float, rate: float, years: float) -> float:
    """
    Calculate the simple interest for a given principal, rate, and time in years.

    Args:
        principal (float): The principal amount.
        rate (float): The annual interest rate in percentage.
        years (float): The time in years.

    Returns:
        float: The calculated simple interest.
    """
    return principal * years * rate / 100


def uppercase_count(s: str) -> int:
    """
    Count the number of uppercase letters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The number of uppercase letters in the string.
    """
    upper_count = 0
    for letter in s:
        if letter.isupper():
            upper_count += 1

    return upper_count


def distance_between_points(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Calculate the Euclidean distance between two points (x1, y1) and (x2, y2).

    Args:
        x1 (float): The x-coordinate of the first point.
        y1 (float): The y-coordinate of the first point.
        x2 (float): The x-coordinate of the second point.
        y2 (float): The y-coordinate of the second point.

    Returns:
        float: The Euclidean distance between the two points.
    """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
