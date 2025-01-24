import os

from lab5 import analyze_bank_data, analyze_employee_data, analyze_sales_data


class Paths:
    CURRENT_DIR = os.getcwd()
    DATA_PATH = os.path.join(CURRENT_DIR, "test_data")
    EMPLOYEE_DATA_PATH = os.path.join(DATA_PATH, "employee_data")
    SALES_DATA_PATH = os.path.join(DATA_PATH, "sales_data")
    BANK_DATA_PATH = os.path.join(DATA_PATH, "bank_data")


def test_employee_data(file_name, expected_output):
    file_path = os.path.join(Paths.EMPLOYEE_DATA_PATH, file_name)
    result = analyze_employee_data(file_path)
    assert result == expected_output


def test_sales_data(file_name, expected_output):
    file_path = os.path.join(Paths.SALES_DATA_PATH, file_name)
    result = analyze_sales_data(file_path)
    sorted_result = (result[0], result[1], result[2], sorted(result[3]))
    sorted_expected = (expected_output[0], expected_output[1], expected_output[2], sorted(expected_output[3]))
    assert sorted_result == sorted_expected


def test_bank_data(file_name, expected_output):
    file_path = os.path.join(Paths.BANK_DATA_PATH, file_name)
    result = analyze_bank_data(file_path)
    sorted_result = {
        "only_deposit": sorted(result["only_deposit"]),
        "common": sorted(result["common"]),
        "only_withdrawal": sorted(result["only_withdrawal"]),
        "exclusive_count": result["exclusive_count"],
    }
    sorted_expected = {
        "only_deposit": sorted(expected_output["only_deposit"]),
        "common": sorted(expected_output["common"]),
        "only_withdrawal": sorted(expected_output["only_withdrawal"]),
        "exclusive_count": expected_output["exclusive_count"],
    }
    assert sorted_result == sorted_expected


if __name__ == "__main__":
    test_employee_data(
        "data_1.csv",
        (
            4,
            {"Male": 2, "Female": 2},
            "Entry Level",
            [(93, "Female"), (93, "Male")],
        ),
    )

    test_sales_data(
        "data_1.csv",
        (
            {"Electronics": 4, "Clothing": 3, "Home": 3},
            {"North": 400.19, "South": 175.61, "East": 260.03, "West": 250.25},
            500.00,
            ["P005", "P008"],
        ),
    )

    test_bank_data(
        "data_1.csv",
        {
            "only_deposit": ["salary", "gift", "bonus"],
            "common": ["rent"],
            "only_withdrawal": ["groceries", "phone bill"],
            "exclusive_count": 5,
        },
    )
