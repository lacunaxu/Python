import json
import xml.etree.ElementTree as ET
from typing import Dict, List

import requests
from bs4 import BeautifulSoup


def parse_hospital_data(url: str, city_name: str) -> List[dict]:
    """
    Retrieve hospital data from a provided API URL for a specified city.

    Args:
        url (str): The API URL to fetch hospital data.
        city_name (str): The name of the city to filter hospitals.

    Returns:
        List[dict]: A list of dictionaries containing hospital data for the specified city.

    Raises:
        Exception: If the 'city' key is missing in the JSON or the city does not exist.
        Exception: If any required keys are missing from the hospital data.
    """
    r = requests.get(url)
    r.raise_for_status()
    info = r.json()
    
    required_keys = [
        "hospital_id", "hospital_org_id", "ein", "name",
        "street_address", "city", "state", "zip_code",
        "hospital_bed_count", "chrch_affl_f", "urban_location_f",
        "children_hospital_f", "medicare_provider_number", "county",
        "hospital_bed_size", "updated_dt", "fips_state_and_county_code",
        "memb_counc_teach_hosps_f", "name_cr"
    ]
    
    hospital_list = []
    for hospital in info:
        if 'city' not in hospital:
            raise Exception("required key 'city' is missing from the JSON")

        if hospital['city'] == city_name:
            for key in required_keys:
                if key not in hospital:
                    raise Exception(f"required key {key} is missing from the JSON")
            
            hospital_info = {key: hospital[key] for key in required_keys}
            hospital_list.append(hospital_info)
            
    if not hospital_list:
        raise Exception(f"Specified {city_name} does not exist")
    
    return hospital_list


def combine_country_covid_data_from_file(file_name: str) -> str:
    """
    Combine country details and COVID-19 statistics based on country codes from a file.

    Args:
        file_name (str): The file containing country codes, one per line.

    Returns:
        str: A JSON-formatted string containing combined country and COVID-19 data.

    Raises:
        Exception: If the specified file is not found.
        Exception: If a country code does not exist or required keys are missing.
    """
    try:
        country_codes = []
        with open(file_name, 'r') as file:
            for line in file:
                country_codes.append(line.strip().upper())
    except FileNotFoundError:
        raise Exception("The specified file was not found.")
    
    combined_data = []
    for code in country_codes:
        try: 
            country_response = requests.get(f"https://restcountries.com/v3.1/alpha/{code}")
            if country_response.status_code != 200:
                raise Exception("specified country_code does not exist.")
            country_data = country_response.json()[0]

            covid_response = requests.get(f"https://disease.sh/v3/covid-19/countries/{code}")
            if covid_response.status_code != 200:
                raise Exception("specified country_code does not exist.")
            covid_data = covid_response.json()

            combined_data.append({
                'country_code': code,
                'official_name': country_data['name']['official'],
                'latitude': float(country_data['latlng'][0]),
                'longitude': float(country_data['latlng'][1]),
                'population': int(country_data['population']),
                'area': int(country_data['area']),
                'cases': covid_data['cases'],
                'deaths': covid_data['deaths']
            })
        
        except KeyError as e:
            raise Exception(f"Missing key {e}")
        except IndexError:
            raise Exception("specified country_code does not exist.")
        
    return json.dumps(combined_data)


def parse_student_data(file_path: str, student_id: str) -> Dict:
    """
    Parse student data from an XML file and retrieve details for a specific student ID.

    Args:
        file_path (str): The path to the XML file containing student data.
        student_id (str): The ID of the student to retrieve data for.

    Returns:
        Dict: A dictionary containing the student's details and course information.

    Raises:
        Exception: If the student ID is not found in the XML file.
    """
    tree = ET.parse(file_path)

    student_details = {}
    course_details = []

    for student in tree.findall("student"):
        if student.get('id') == student_id:
            student_details = {
                'Name': student.find('name').text,
                'Major': student.find('major').text,
                'Phone': student.find('phone').text,
                'Email': student.find('email').text
            }
            
            courses = student.find('courses')
            for course in courses.findall('course'):
                course_details.append({
                    'CourseName': course.find('course_name').text,
                    'Credits': course.find('credits').text
                })

    if not student_details:
        raise Exception("Student ID not found")

    return {'student_details': student_details, 'course_details': course_details}
