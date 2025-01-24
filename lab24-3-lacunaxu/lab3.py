import string


def compute_persistence(num: int) -> int:
    """
    Compute the persistence of a number.

    Args: num (int): input number that needs to be non-negative integer

    Returns: int the persistence of a number
    """

    if type(num) is not int or num < 0:
        raise Exception("Invalid input")
    
    steps = 0
    temp_num = num
    
    while(temp_num >= 10):
        
        product = 1
        
        while temp_num > 0:
            product *= (temp_num%10)
            temp_num = temp_num//10
        
        temp_num = product 
        steps += 1            
        
    return steps


def is_digit_power_sum(num: int, power: int) -> bool:
    """
    Check if the number can be represented as the sum of its digits raised 
    to a given power.

    Args: num(int): the non-negative integer
    power(int): the non-negative integer exponent

    Returns: (bool) true if the number equals to be sum of each number raised 
    to the given power False otherwise
    """
    if type(num) is not int or type(power) is not int:
        raise Exception("Invalid input") 
    if num < 0 or power < 0:
        raise Exception("Invalid input")
        
    sums = 0
    temp_num = num
    
    while temp_num > 0:
        sums += (temp_num%10)**power
        temp_num = temp_num//10      
    
    
    return sums == num


def is_valid_product_code(code: str) -> bool:
    """
    Check if the product code is valid.

    Args: code(str): The product code to validate

    Returns: true if the product code is valid, False otherwise
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