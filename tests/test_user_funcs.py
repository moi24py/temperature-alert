import pytest
from unittest.mock import patch

import packages.user_funcs as u_fun

def test_get_loc_with_valid_input():
    """Test the get input function with a valid input"""
    with patch('builtins.input', return_value='Berlin'):
        u_fun.get_loc('city') == 'Berlin'

def test_get_loc_type_error():
    # Mock dell'input per restituire un valore non valido
    with patch('builtins.input', return_value='$invalid$'):
        # Usa pytest.raises per verificare che venga sollevato TypeError
        with pytest.raises(TypeError):
            u_fun.get_loc('city')

def test_get_temp_with_valid_input():
    """Test the get input function with a valid input"""
    with patch('builtins.input', return_value='18'):
        u_fun.get_temp() == '18.0'

def test_get_temp_with_invalid_input():
    """Test the get input function with a valid input"""
    with patch('builtins.input', return_value='abc'):
        with pytest.raises(TypeError):
            u_fun.get_temp()

def test_get_criteria_valid_input():
    """Test the function with a valid input"""
    with patch('builtins.input', return_value='below'):
        u_fun.get_criteria(18.0,'c')

def test_get_criteria_invalid_input():
    """Test the function with a valid input"""
    with patch('builtins.input', return_value='abo'):
        with pytest.raises(TypeError):
            u_fun.get_criteria(18.0,'c')

def test_temp_unit_valid_input():
    """Test the function with a valid input"""
    with patch('builtins.input', return_value=('c')):
        unit = u_fun.temp_unit()
        assert unit == ('c','')

def test_temp_unit_invalid_input():
    """Test the function with an invalid input"""
    with patch('builtins.input', return_value='s'):
        with pytest.raises(ValueError):
            u_fun.temp_unit()

def test_user_valid_inputs():
    """Test the function with a valid input"""
    with patch('builtins.input', side_effect=('Berlin','Germany','18.0','c','below')):
        u_fun.user_inputs()

def test_choose_city_valid_input():
    """Test function with valid inputs"""
    cities = [
        {'city': 'Masan', 'city_ascii': 'Masan', 'lat': '35.1833', 'lng': '128.5500', 'country': 'Korea, South', 'iso2': 'KR', 'iso3': 'KOR', 'admin_name': 'Gyeongnam', 'capital': '', 'population': '179266', 'id': '1410394650'},
        {'city': 'Manpo', 'city_ascii': 'Manpo', 'lat': '41.1570', 'lng': '126.2900', 'country': 'Korea, North', 'iso2': 'KP', 'iso3': 'PRK', 'admin_name': 'Chagang', 'capital': '', 'population': '116760', 'id': '1408334845'}
        ]
    with patch('builtins.input', return_value=1):
        city = u_fun.choose_city(cities)
        assert city == cities[1]

def test_choose_city_invalid_input():
    """Test function with valid inputs"""
    cities = [
        {'city': 'Masan', 'city_ascii': 'Masan', 'lat': '35.1833', 'lng': '128.5500', 'country': 'Korea, South', 'iso2': 'KR', 'iso3': 'KOR', 'admin_name': 'Gyeongnam', 'capital': '', 'population': '179266', 'id': '1410394650'},
        {'city': 'Manpo', 'city_ascii': 'Manpo', 'lat': '41.1570', 'lng': '126.2900', 'country': 'Korea, North', 'iso2': 'KP', 'iso3': 'PRK', 'admin_name': 'Chagang', 'capital': '', 'population': '116760', 'id': '1408334845'}
        ]
    with patch('builtins.input', return_value='abc'):
        with pytest.raises(TypeError):
            u_fun.choose_city(cities)

def test_print_or_send_valid_input():
    """Test function with valid inputs"""
    with patch('builtins.input', return_value='s'):
        res = u_fun.print_or_send()
        assert res == 's'

def test_print_or_send_invalid_input():
    """Test function with invalid inputs"""
    with patch('builtins.input', return_value=2):
        with pytest.raises(TypeError):
            u_fun.print_or_send()
