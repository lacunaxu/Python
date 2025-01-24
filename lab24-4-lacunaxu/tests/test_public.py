import os

import pytest
from lab4 import anagram_finder, find_max_in_lines, log_file_categorizer


class Path:
    CURRENT_WORKING_DIR = os.getcwd()
    TEST_DATA_PATH = os.path.join(CURRENT_WORKING_DIR, "test_data")
    FUNCTION1_TXT_FILES_PATH = os.path.join(TEST_DATA_PATH, "max_in_lines")
    FUNCTION2_TXT_FILES_PATH = os.path.join(TEST_DATA_PATH, "anagram")
    FUNCTION3_TXT_FILES_PATH = os.path.join(TEST_DATA_PATH, "log_file")


@pytest.mark.parametrize(
    "file_name, expected_result",
    [
        ("numbers1.txt", [7, 9, 4]),
        ("numbers2.txt", [5, 100, 60]),
        ("numbers3.txt", [10, 30, -1]),
        ("numbers4.txt", []),
        ("numbers6.txt", [4, 23, 5, 89]),
    ],
)
@pytest.mark.timeout(0.3)
def test_find_max_in_lines_valid(file_name, expected_result):
    file_name = os.path.join(Path.FUNCTION1_TXT_FILES_PATH, file_name)
    assert find_max_in_lines(file_name) == expected_result


@pytest.mark.parametrize(
    "file_name",
    [
        ("numbers5.txt"),
    ],
)
@pytest.mark.timeout(0.3)
def test_find_max_in_lines_file_not_found(file_name):
    file_name = os.path.join(Path.FUNCTION1_TXT_FILES_PATH, file_name)
    with pytest.raises(Exception, match="File Not Found"):
        find_max_in_lines(file_name)


@pytest.mark.parametrize(
    "file_name, expected_output_file, expected_contents",
    [
        (
            "sample_file1.txt",
            "anagrams_sample_file1.txt",
            ["listen,silent", "-", "dusty,study", "evil,live rat,art"],
        ),
        (
            "sample_file2.txt",
            "anagrams_sample_file2.txt",
            ["-", "-", "tar,rat act,cat", "-"],
        ),
        ("sample_file4.txt", "anagrams_sample_file4.txt", []),
    ],
)
@pytest.mark.timeout(0.3)
def test_anagram_finder_valid(file_name, expected_output_file, expected_contents):
    anagram_finder(os.path.join(Path.FUNCTION2_TXT_FILES_PATH, file_name))

    expected_output_file = os.path.join(Path.FUNCTION2_TXT_FILES_PATH, expected_output_file)
    with open(expected_output_file, "r") as output_file:
        output_lines = output_file.read().splitlines()

    assert output_lines == expected_contents


@pytest.mark.parametrize(
    "file_name",
    [
        ("sample_file3.txt"),
    ],
)
@pytest.mark.timeout(0.3)
def test_anagram_finder_file_not_found(file_name):
    with pytest.raises(Exception, match="File Not Found"):
        anagram_finder(os.path.join(Path.FUNCTION2_TXT_FILES_PATH, file_name))


@pytest.mark.parametrize(
    "file_name, expected_error_output, expected_info_output, expected_warning_output, expected_error_contents,"
    "expected_info_contents, expected_warning_contents",
    [
        (
            "log.txt",
            "error_log.txt",
            "info_log.txt",
            "warning_log.txt",
            ["ERROR: Disk space is full", "ERROR: File not found"],
            ["INFO: User logged in", "INFO: System reboot initiated"],
            ["WARNING: Low memory"],
        ),
        (
            "server_log.txt",
            "error_server_log.txt",
            "info_server_log.txt",
            "warning_server_log.txt",
            ["ERROR: Connection timed out", "ERROR: Unable to reach host"],
            [
                "INFO: Server started",
                "INFO: Database connected",
                "INFO: Server running",
            ],
            ["WARNING: High CPU usage detected"],
        ),
        (
            "empty_log.txt",
            "error_empty_log.txt",
            "info_empty_log.txt",
            "warning_empty_log.txt",
            [],
            [],
            [],
        ),
    ],
)
@pytest.mark.timeout(0.3)
def test_log_file_categorizer_valid(
    file_name,
    expected_error_output,
    expected_info_output,
    expected_warning_output,
    expected_error_contents,
    expected_info_contents,
    expected_warning_contents,
):
    log_file_categorizer(os.path.join(Path.FUNCTION3_TXT_FILES_PATH, file_name))

    # Helper function to read and assert log files
    def check_file_contents(file_path, expected_contents):
        with open(file_path, "r") as file:
            lines = file.read().splitlines()
        assert lines == expected_contents

    # Check the contents of each log file
    check_file_contents(os.path.join(Path.FUNCTION3_TXT_FILES_PATH, expected_error_output), expected_error_contents)
    check_file_contents(os.path.join(Path.FUNCTION3_TXT_FILES_PATH, expected_info_output), expected_info_contents)
    check_file_contents(os.path.join(Path.FUNCTION3_TXT_FILES_PATH, expected_warning_output), expected_warning_contents)


@pytest.mark.parametrize(
    "file_name",
    [
        ("invalid_log.txt"),
    ],
)
@pytest.mark.timeout(0.3)
def test_log_file_categorizer_file_not_found(file_name):
    with pytest.raises(Exception, match="File Not Found"):
        log_file_categorizer(os.path.join(Path.FUNCTION3_TXT_FILES_PATH, file_name))
