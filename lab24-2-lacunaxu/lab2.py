from typing import List, Tuple


def format_date(day: int, month: int, year: int) -> str:
    """
    Format the date as per the structure provided.
    """
    month_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    big_month = [1,3,5,7,8,10,12]
    small_month = [4,6,9,11]
    if day <= 0 or month <= 0 or month > 12:
        raise Exception(f'The given date: {day}, {month}, {year} is invalid')

    if month in big_month and day > 31:
        raise Exception(f'The given date: {day}, {month}, {year} is invalid')
    elif month in small_month and day > 30:
        raise Exception(f'The given date: {day}, {month}, {year} is invalid')

    if year < 1000 or year > 3000:
        raise Exception(f'The given date: {day}, {month}, {year} is invalid')

    if month == 2:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            if day > 29:
                raise Exception(f'The given date: {day}, {month}, {year} is invalid')
        elif day > 28:
            raise Exception(f'The given date: {day}, {month}, {year} is invalid')
        
    newmonth = month_name[month - 1]
    newday = "{:02}".format(day)
    return f"{newday} {newmonth}, {year}"



def check_palindrome_tuples(tups: List[Tuple[str, str]]) -> bool:
    """
    Find the palindrome word tuples in the list.
    """
    if type(tups) is not list:
        raise Exception("Invalid Input")

    for item_tups in tups:
        if type(item_tups) is not tuple or len(item_tups) != 2:
            raise Exception("Invalid Input")
            
        for item_string in item_tups:
            if type(item_string) is not str or len(item_string) <= 1:
                raise Exception("Invalid Input")
                
    for first, second in tups:
        if second != first[::-1]:
            return False
    return True
    
    


def join_by_delimiter(substrings: List[str], delimiter: str) -> str:
    """
    Join the substrings using a delimiter provided.
    """
    temp = ""
    
    if type(delimiter) is not str or len(delimiter) > 1:
        raise Exception("Invalid Input")
    
    if type(substrings) is not list:
        raise Exception("Invalid Input")
    
    if len(substrings) > 1:
        for i in range(len(substrings)):
            if type(substrings[i]) is not str:
                raise Exception("Invalid Input")

            if i == len(substrings)-1:
                temp += substrings[i]
            else:
                temp += substrings[i] + delimiter
        return temp
    
    elif len(substrings) == 0:
        return ""
        
    elif len(substrings) == 1:
        return substrings[0]
