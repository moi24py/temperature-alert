import pytest
from unittest.mock import patch, mock_open
import sys

import modules.app_funcs as a_fun

def test_get_db_cities_if_file_found():
    """Tests if the function can open and read a file"""
    mock_csv_data = "city,country\nRome,Italy\nParis,France"
    with patch("os.path.isfile", return_value=True):
        with patch("builtins.open", mock_open(read_data=mock_csv_data)):
            result = a_fun.get_db_cities("worldcities.csv")
            expected_result = [{'city': 'Rome', 'country': 'Italy'}, {'city': 'Paris', 'country': 'France'}]
            assert result == expected_result


def test_get_db_cities_file_not_found():
    """Tests if the function raises an error"""
    with patch("os.path.isfile", return_value=False):
        with pytest.raises(FileNotFoundError):
            a_fun.get_db_cities("worldcities.csv")


def test_search_city_with_matching_data():
    """Tests if the function searches in the database and find matching cities"""
    cities = [
        {'city': 'Kamikawa', 'city_ascii': 'Kamikawa', 'lat': '36.2139', 'lng': '139.1017', 'country': 'Japan',
         'iso2': 'JP', 'iso3': 'JPN', 'admin_name': 'Saitama', 'capital': '', 'population': '13077', 'id': '1392003364'},
        {'city': 'Kamikawa', 'city_ascii': 'Kamikawa', 'lat': '35.0667', 'lng': '134.7333', 'country': 'Japan',
         'iso2': 'JP', 'iso3': 'JPN', 'admin_name': 'Hyōgo', 'capital': '', 'population': '10557', 'id': '1392003365'},
        {'city': 'Kamikita-kita', 'city_ascii': 'Kamikita-kita', 'lat': '40.7360', 'lng': '140.9560', 'country': 'Japan',
         'iso2': 'JP', 'iso3': 'JPN', 'admin_name': 'Aomori', 'capital': '', 'population': '9830', 'id': '1392618697'}
    ]
  
    matching_cities = a_fun.search_city('kamik','Japan')
    assert matching_cities == cities

def test_search_city_with_no_matching_data():
    """Tests if the function searches in the database but cannot find matching cities"""
    matching_cities = a_fun.search_city('iou','pol')
    assert matching_cities == None
