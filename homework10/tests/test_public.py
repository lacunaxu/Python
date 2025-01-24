import json
import os
from lab10 import combine_country_covid_data_from_file, parse_hospital_data, parse_student_data

def test_parse_hospital_data_opp():
    """Test parsing hospital data for a specific city."""
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

    result = parse_hospital_data(url, "Opp")
    assert result == expected_result

def test_parse_hospital_data_non_existent_city():
    """Test parsing hospital data for a non-existent city."""
    url = "https://www.communitybenefitinsight.org/api/get_hospitals.php"
    try:
        parse_hospital_data(url, "NonExistentCity")
    except Exception as e:
        assert str(e) == "Specified NonExistentCity does not exist"

def test_combine_country_covid_data_valid():
    """Test combining country COVID data from a valid file."""
    file_name = "countries.txt"
    file_path = os.path.join("test_data", "country_covid", file_name)
    expected_result = json.dumps(
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
        ]
    )

    result = combine_country_covid_data_from_file(file_path)
    assert result == expected_result

def test_combine_country_covid_data_invalid():
    """Test combining country COVID data from an invalid file."""
    file_name = "invalid_countries.txt"
    file_path = os.path.join("test_data", "country_covid", file_name)
    try:
        combine_country_covid_data_from_file(file_path)
    except Exception as e:
        assert "specified country_code does not exist." in str(e)

def test_parse_student_data():
    """Test parsing student data from an XML file."""
    file_path = os.path.join("test_data", "student_xml", "students.xml")

    student_id = "S123"
    expected_result = {
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
    }

    result = parse_student_data(file_path, student_id)
    assert result == expected_result

    student_id_invalid = "S999"
    try:
        parse_student_data(file_path, student_id_invalid)
    except Exception as e:
        assert "Student ID not found" in str(e)

if __name__ == "__main__":
    test_parse_hospital_data_opp()
    test_parse_hospital_data_non_existent_city()
    test_combine_country_covid_data_valid()
    test_combine_country_covid_data_invalid()
    test_parse_student_data()
    print("All tests passed.")
