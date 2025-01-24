import json
import os

import pytest

from lab10 import combine_country_covid_data_from_file, parse_hospital_data, parse_student_data


class Path:
    CURRENT_WORKING_DIR = os.getcwd()
    TEST_DATA_PATH = os.path.join(CURRENT_WORKING_DIR, "test_data")
    COUNTRY_COVID_DATA_PATH = os.path.join(TEST_DATA_PATH, "country_covid")
    STUDENT_XML_PATH = os.path.join(TEST_DATA_PATH, "student_xml")


@pytest.mark.timeout(5)
def test_parse_hospital_data_opp():
    url = "https://www.communitybenefitinsight.org/api/get_hospitals.php"
    expected_result = [
        {
            "hospital_id": "1",
            "hospital_org_id": "1",
            "ein": "630307951",
            "name": "Mizell Memorial Hospital",
            "name_cr": "Mizell Memorial Hospital",
            "street_address": "702 Main Street",
            "city": "Opp",
            "state": "AL",
            "zip_code": "36462",
            "fips_state_and_county_code": "01039",
            "hospital_bed_count": "99",
            "chrch_affl_f": "N",
            "urban_location_f": "N",
            "children_hospital_f": "N",
            "memb_counc_teach_hosps_f": "N",
            "medicare_provider_number": "010007",
            "county": "Covington County",
            "hospital_bed_size": "<100 beds",
            "updated_dt": "November 20, 2023",
        }
    ]
    assert parse_hospital_data(url, "Opp") == expected_result


@pytest.mark.timeout(5)
def test_parse_hospital_data_non_existent_city():
    url = "https://www.communitybenefitinsight.org/api/get_hospitals.php"
    with pytest.raises(Exception, match="Specified NonExistentCity does not exist"):
        parse_hospital_data(url, "NonExistentCity")


@pytest.mark.parametrize(
    "file_name, expected_result",
    [
        (
            "countries.txt",
            json.dumps(
                [
                    {
                        "country_code": "US",
                        "official_name": "United States of America",
                        "latitude": 38.0,
                        "longitude": -97.0,
                        "population": 329484123,
                        "area": 9372610,
                        "cases": 111820082,
                        "deaths": 1219487,
                    },
                    {
                        "country_code": "IN",
                        "official_name": "Republic of India",
                        "latitude": 20.0,
                        "longitude": 77.0,
                        "population": 1380004385,
                        "area": 3287590,
                        "cases": 45035393,
                        "deaths": 533570,
                    },
                    {
                        "country_code": "CA",
                        "official_name": "Canada",
                        "latitude": 60.0,
                        "longitude": -95.0,
                        "population": 38005238,
                        "area": 9984670,
                        "cases": 4946090,
                        "deaths": 59034,
                    },
                    {
                        "country_code": "GB",
                        "official_name": "United Kingdom of Great Britain and Northern Ireland",
                        "latitude": 54.0,
                        "longitude": -2.0,
                        "population": 67215293,
                        "area": 242900,
                        "cases": 24910387,
                        "deaths": 232112,
                    },
                ]
            ),
        ),
    ],
)
@pytest.mark.timeout(10)
def test_combine_country_covid_data_valid(file_name, expected_result):
    file_name = os.path.join(Path.COUNTRY_COVID_DATA_PATH, file_name)
    assert combine_country_covid_data_from_file(file_name) == expected_result


@pytest.mark.parametrize(
    "file_name",
    [
        "invalid_countries.txt",
    ],
)
@pytest.mark.timeout(5)
def test_combine_country_covid_data_invalid(file_name):
    file_name = os.path.join(Path.COUNTRY_COVID_DATA_PATH, file_name)
    with pytest.raises(Exception, match="specified country_code does not exist."):
        combine_country_covid_data_from_file(file_name)


@pytest.mark.parametrize(
    "file_path, student_id, expected_result",
    [
        (
            "students.xml",
            "S123",
            {
                "student_details": {
                    "Name": "Alice Johnson",
                    "Major": "Computer Science",
                    "Phone": "(555) 987-6543",
                    "Email": "alice.johnson@example.com",
                },
                "course_details": [
                    {"CourseName": "Data Structures", "Credits": "3"},
                    {"CourseName": "Operating Systems", "Credits": "4"},
                ],
            },
        ),
        ("students.xml", "S999", {}),
    ],
)
@pytest.mark.timeout(3)
def test_parse_student_data_valid(file_path, student_id, expected_result):
    file_path = os.path.join(Path.STUDENT_XML_PATH, file_path)
    if student_id == "S999":
        with pytest.raises(Exception, match="Student ID not found"):
            parse_student_data(file_path, student_id)
    else:
        result = parse_student_data(file_path, student_id)
        assert result == expected_result
