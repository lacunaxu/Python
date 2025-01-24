import os
from lab4 import find_max_in_lines, anagram_finder, log_file_categorizer

class Path:
    CURRENT_WORKING_DIR = os.getcwd()
    TEST_DATA_PATH = os.path.join(CURRENT_WORKING_DIR, "test_data")
    MAX_IN_LINES_PATH = os.path.join(TEST_DATA_PATH, "max_in_lines")
    ANAGRAMS_PATH = os.path.join(TEST_DATA_PATH, "anagram")
    LOG_FILES_PATH = os.path.join(TEST_DATA_PATH, "log_file")


def find_max_in_lines(file_name: str):
    """
    Find the maximum number in each line of a file containing numeric values.

    Args:
        file_name (str): Path to the file.

    Returns:
        List[int]: List of maximum numbers from each line. If a line is empty, it is skipped.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.exists(file_name):
        raise FileNotFoundError("The specified file does not exist.")

    max_values = []

    with open(file_name, "r") as file:
        for line in file:
            try:
                numbers = list(map(int, line.split()))
                if numbers:
                    max_values.append(max(numbers))
            except ValueError:
                continue  # Skip lines with non-numeric data

    return max_values


def anagram_finder(input_file: str, output_file: str):
    """
    Find anagrams in the input file and write them to an output file.

    Args:
        input_file (str): Path to the input file containing words.
        output_file (str): Path to the output file to save anagrams.

    Raises:
        FileNotFoundError: If the input file does not exist.
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError("The specified input file does not exist.")

    anagrams = []

    with open(input_file, "r") as file:
        for line in file:
            words = line.strip().split(",")
            grouped = {}
            for word in words:
                sorted_word = "".join(sorted(word.strip()))
                if sorted_word in grouped:
                    grouped[sorted_word].append(word.strip())
                else:
                    grouped[sorted_word] = [word.strip()]

            for group in grouped.values():
                if len(group) > 1:
                    anagrams.append(",".join(group))

    with open(output_file, "w") as out_file:
        if anagrams:
            out_file.write("\n".join(anagrams))
        else:
            out_file.write("-")


def log_file_categorizer(file_name: str, error_file: str, info_file: str, warning_file: str):
    """
    Categorize log messages into error, info, and warning logs.

    Args:
        file_name (str): Path to the log file.
        error_file (str): Path to save error messages.
        info_file (str): Path to save info messages.
        warning_file (str): Path to save warning messages.

    Raises:
        FileNotFoundError: If the log file does not exist.
    """
    if not os.path.exists(file_name):
        raise FileNotFoundError("The specified log file does not exist.")

    error_logs = []
    info_logs = []
    warning_logs = []

    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("ERROR:"):
                error_logs.append(line)
            elif line.startswith("INFO:"):
                info_logs.append(line)
            elif line.startswith("WARNING:"):
                warning_logs.append(line)

    # Write categorized logs to their respective files
    with open(error_file, "w") as ef:
        ef.write("\n".join(error_logs))

    with open(info_file, "w") as inf:
        inf.write("\n".join(info_logs))

    with open(warning_file, "w") as wf:
        wf.write("\n".join(warning_logs))


# Example usage:
if __name__ == "__main__":
    # Example for find_max_in_lines
    try:
        max_numbers = find_max_in_lines(os.path.join(Path.MAX_IN_LINES_PATH, "numbers1.txt"))
        print("Max numbers in each line:", max_numbers)
    except FileNotFoundError as e:
        print(e)

    # Example for anagram_finder
    try:
        anagram_finder(
            os.path.join(Path.ANAGRAMS_PATH, "sample_file1.txt"),
            os.path.join(Path.ANAGRAMS_PATH, "anagrams_sample_file1.txt"),
        )
        print("Anagrams written to output file.")
    except FileNotFoundError as e:
        print(e)

    # Example for log_file_categorizer
    try:
        log_file_categorizer(
            os.path.join(Path.LOG_FILES_PATH, "log.txt"),
            os.path.join(Path.LOG_FILES_PATH, "error_log.txt"),
            os.path.join(Path.LOG_FILES_PATH, "info_log.txt"),
            os.path.join(Path.LOG_FILES_PATH, "warning_log.txt"),
        )
        print("Log files categorized successfully.")
    except FileNotFoundError as e:
        print(e)
