import os
import string
from typing import List


def find_max_in_lines(file_name: str) -> List[int]:
    """
    Implement a function that reads a file, finds the maximum 
    integer in each line, and appends it to a list.
    
    Args: file_name(str): The name of the input text file where 
    each line contains multiple integers.
    
    return: list(int): A list of integers, where each element 
    corresponds to the maximum integer from each line in the file.
    """
    try:
    
        with open(file_name, 'r') as file_handle:
            max_vector = []

            for line in file_handle:

                if(line != '\n'):
                    list_str_line = line.split(',')
                    numbers = [int(i) for i in list_str_line]
                    max_vector.append(max(numbers))

    
    except FileNotFoundError:
        raise Exception("File Not Found")
    
    return max_vector



def anagram_finder(file_name: str) -> None:
    """
    Implement a function that finds anagram pairs from the input file and write the 
    result to output file.
    
    Args: file_name(str): The name of the input text file that 
    contains sentences to check for anagrams.
    
    Return: None The function does not return anything but will 
    create a new file with the name anagrams_{file_name}
    
    """
    try:
        # Create the output file path in the same directory as the input file
        output_file_name = os.path.join(os.path.dirname(file_name), f"anagrams_{os.path.basename(file_name)}")
        
        with open(file_name, 'r') as input_file:
            with open(output_file_name, 'w') as output_file:
                for line in input_file:
                    line = line.lower().strip()
                    cleaned_line = ''.join([char for char in line if char not in string.punctuation])
                    words = cleaned_line.split()

                    no_duplicate_words = [word for word in words if words.count(word) == 1]
                    sorted_words = [''.join(sorted(word)) for word in no_duplicate_words]

                    anagrams_dict = {}
                    for i, sorted_word in enumerate(sorted_words):
                        if sorted_words.count(sorted_word) > 1:
                            if sorted_word in anagrams_dict:
                                anagrams_dict[sorted_word].append(no_duplicate_words[i])
                            else:
                                anagrams_dict[sorted_word] = [no_duplicate_words[i]]

                    if not anagrams_dict:
                        output_file.write('-\n')
                    else:
                        result = ' '.join([','.join(v) for v in anagrams_dict.values()])
                        output_file.write(result + '\n')
                
    except FileNotFoundError:
        raise Exception("File Not Found")


def log_file_categorizer(file_name: str) -> None:
    """
    Implement a function to categorize the log entries based on the event types.
    
    Args: file_name(str): The name of the input text file that 
    contains sentences to check for anagrams.
    
    Returns: None The function does not return anything but will 
    create a new file with the name anagrams_{file_name}
    """
    try:
        with open(file_name, 'r') as input_file:
            error_file_name = os.path.join(os.path.dirname(file_name), f"error_{os.path.basename(file_name)}")
            info_file_name = os.path.join(os.path.dirname(file_name), f"info_{os.path.basename(file_name)}")
            warning_file_name = os.path.join(os.path.dirname(file_name), f"warning_{os.path.basename(file_name)}")

            with open(error_file_name, 'w') as error_file, \
                 open(info_file_name, 'w') as info_file, \
                 open(warning_file_name, 'w') as warning_file:

                for line in input_file:
                    line = line.strip()  # Remove leading/trailing whitespace

                    cleaned_line = ''.join([char for char in line if char not in 
                                    string.punctuation])
                    first_word = cleaned_line.split()[0]
            
                    if first_word == "ERROR":
                        error_file.write(line + '\n')
                    elif first_word == ("INFO"):
                        info_file.write(line + '\n')
                    elif first_word == ("WARNING"):
                        warning_file.write(line + '\n')

    except FileNotFoundError:
        raise Exception("File Not Found")
    