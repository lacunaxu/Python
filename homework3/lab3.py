import string


def compute_persistence(num: int) -> int:
    """
    Compute the persistence of a number.

    Persistence is the number of steps required to reduce a number to a single digit
    by multiplying all of its digits repeatedly.

    Args:
        num (int): The input number. It must be a non-negative integer.

    Returns:
        int: The persistence of the number.

    Raises:
        Exception: If the input is not a non-negative integer.
    """
    if type(num) is not int or num < 0:
        raise Exception("Invalid input")
    
    steps = 0
    temp_num = num
    
    while(temp_num >= 10):
        product = 1
        
        while temp_num > 0:
            product *= (temp_num % 10)
            temp_num = temp_num // 10
        
        temp_num = product 
        steps += 1            
        
    return steps


def is_digit_power_sum(num: int, power: int) -> bool:
    """
    Check if the number can be represented as the sum of its digits raised to a given power.

    Args:
        num (int): The input number. It must be a non-negative integer.
        power (int): The power to which each digit is raised. It must be a non-negative integer.

    Returns:
        bool: True if the number equals the sum of its digits raised to the given power.
              False otherwise.

    Raises:
        Exception: If the inputs are not non-negative integers.
    """
    if type(num) is not int or type(power) is not int:
        raise Exception("Invalid input") 
    if num < 0 or power < 0:
        raise Exception("Invalid input")
        
    sums = 0
    temp_num = num
    
    while temp_num > 0:
        sums += (temp_num % 10) ** power
        temp_num = temp_num // 10      
    
    return sums == num


def is_valid_product_code(code: str) -> bool:
    """
    Check if the product code is valid.

    A valid product code must meet the following criteria:
    1. The code must be exactly 12 characters long.
    2. It must contain at least two uppercase letters and three digits.
    3. It must contain exactly one dash ('-'), which cannot be the first or last character.
    4. All characters must be either alphanumeric or a dash.

    Args:
        code (str): The product code to validate.

    Returns:
        bool: True if the product code is valid, False otherwise.

    Raises:
        Exception: If the input is not a string.
    """
    if type(code) is not str:
        raise Exception("Invalid input") 
    
    if len(code) != 12:
        return False
        
    uppercase = 0
    digit = 0
    dash = 0
    
    if code[0] == '-' or code[-1] == '-':
        return False
    
    for i in code:
        if i == '-':
            dash += 1
        elif i.isupper():
            uppercase += 1
        elif i.isdigit():
            digit += 1
        elif not i.isalnum():
            return False
        
    return uppercase >= 2 and digit >= 3 and dash == 1
