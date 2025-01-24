def compute_persistence(num: int) -> int:
    """
    Computes the multiplicative persistence of a number.
    Multiplicative persistence is the number of steps required to reduce
    a number to a single digit by multiplying its digits.
    
    Args:
        num (int): The input number to calculate persistence for.
    
    Returns:
        int: The persistence count (number of multiplication steps).
    
    Raises:
        Exception: If the input is not a positive integer.
    """
    if not isinstance(num, int) or num < 0:
        raise Exception("Invalid input")

    steps = 0
    while num >= 10:
        product = 1
        for digit in str(num):
            product *= int(digit)
        num = product
        steps += 1

    return steps


def is_digit_power_sum(num: int, power: int) -> bool:
    """
    Determines if the number is equal to the sum of its digits
    each raised to the given power.
    
    Args:
        num (int): The input number to check.
        power (int): The power to which each digit is raised.
    
    Returns:
        bool: True if the number is equal to the sum of its digits raised to the power, False otherwise.
    
    Raises:
        Exception: If the inputs are invalid (e.g., negative or non-integers).
    """
    if not isinstance(num, int) or num < 0 or not isinstance(power, int) or power < 0:
        raise Exception("Invalid input")

    digit_power_sum = sum(int(digit) ** power for digit in str(num))
    return digit_power_sum == num


def is_valid_product_code(code: str) -> bool:
    """
    Validates a product code based on the following conditions:
    - The code must have exactly one dash ('-').
    - The code must contain at least 3 uppercase letters.
    - The code must contain at least 2 digits.
    - The code can contain lowercase letters but no special characters.
    
    Args:
        code (str): The product code to validate.
    
    Returns:
        bool: True if the code is valid, False otherwise.
    """
    if not isinstance(code, str):
        raise Exception("Invalid input")

    if code.count("-") != 1:
        return False

    uppercase_count = sum(1 for char in code if char.isupper())
    digit_count = sum(1 for char in code if char.isdigit())

    if uppercase_count < 3 or digit_count < 2:
        return False

    valid_chars = all(char.isalnum() or char == "-" for char in code)
    return valid_chars


# Examples to test the functions:

# Test `compute_persistence`
print(compute_persistence(39))  # Expected: 3
print(compute_persistence(999))  # Expected: 4
print(compute_persistence(4))  # Expected: 0

# Test `is_digit_power_sum`
print(is_digit_power_sum(153, 3))  # Expected: True
print(is_digit_power_sum(9474, 4))  # Expected: True
print(is_digit_power_sum(12, 3))  # Expected: False

# Test `is_valid_product_code`
print(is_valid_product_code("A1B-3456CDEF"))  # Expected: True
print(is_valid_product_code("AbCD1234567-"))  # Expected: False
print(is_valid_product_code("a1-Bc2DEf34g"))  # Expected: True
print(is_valid_product_code("A1Bc2DeF34"))  # Expected: False
print(is_valid_product_code("ABCDE12-FGHI"))  # Expected: False
print(is_valid_product_code("&A907y_Chj-FGHI"))  # Expected: False
