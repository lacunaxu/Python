# Include your imports here
import math


def simple_interest(principal: float, rate: float, years: float) -> float:
    """
    Calculate the simple interest for a given principal, rate, and time in years.
    """
    return principal * years * rate / 100


def uppercase_count(s: str) -> int:
    """
    Count the number of uppercase letters in a given string.
    """
    upper_count = 0
    for letter in s:
        if(letter.isupper()):
            upper_count += 1

    return upper_count


def distance_between_points(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Calculate the Euclidean distance between two points (x1, y1) and (x2, y2).
    """
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)