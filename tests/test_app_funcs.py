import pytest
from unittest.mock import patch, mock_open
import sys

import modules.app_funcs as a_fun

def test_get_db_cities_if_file_found():
    """Tests if the function can open and read a file"""
    mock_csv_data = "city,country\nRome,Italy\nParis,France"
    with patch("os.path.isfile", return_value=True):  # Il file esiste
        with patch("builtins.open", mock_open(read_data=mock_csv_data)):
            result = a_fun.get_db_cities("worldcities.csv")
            expected_result = [{'city': 'Rome', 'country': 'Italy'}, {'city': 'Paris', 'country': 'France'}]
            assert result == expected_result


def test_get_db_cities_file_not_found():
    """Tests if the function raises an error when no file is found"""
    with patch("os.path.isfile", return_value=False):
        with pytest.raises(FileNotFoundError):  # Ci aspettiamo che venga sollevata un'eccezione
            a_fun.get_db_cities("worldcities.csv")


def test_search_city_with_matching_data():
    """Tests if the function can search in the database and find matching cities"""
    cities = [
        {'city': 'Kamikawa', 'city_ascii': 'Kamikawa', 'lat': '36.2139', 'lng': '139.1017', 'country': 'Japan','iso2': 'JP', 'iso3': 'JPN', 'admin_name': 'Saitama', 'capital': '', 'population': '13077', 'id': '1392003364'},
        {'city': 'Kamikawa', 'city_ascii': 'Kamikawa', 'lat': '35.0667', 'lng': '134.7333', 'country': 'Japan', 'iso2': 'JP', 'iso3': 'JPN', 'admin_name': 'Hyōgo', 'capital': '', 'population': '10557', 'id': '1392003365'},
        {'city': 'Kamikita-kita', 'city_ascii': 'Kamikita-kita', 'lat': '40.7360', 'lng': '140.9560', 'country': 'Japan', 'iso2': 'JP', 'iso3': 'JPN', 'admin_name': 'Aomori', 'capital': '', 'population': '9830', 'id': '1392618697'}
    ]
    matching_cities = a_fun.search_city('kamik','Japan')
    assert matching_cities == cities


def test_search_city_with_no_matching_data():
    """Tests if the function can search in the database and but there are no matching cities"""
    matching_cities = a_fun.search_city('iou','pol')
    assert matching_cities == None


def test_get_coords():
    """Tests if the function returns a tuple with the city's latitude and longitude"""
    city = {'city': 'Kamikita-kita', 'city_ascii': 'Kamikita-kita', 'lat': '40.7360', 'lng': '140.9560', 'country': 'Japan', 'iso2': 'JP', 'iso3': 'JPN', 'admin_name': 'Aomori', 'capital': '', 'population': '9830', 'id': '1392618697'}
    lat_long = a_fun.get_coords(city)
    assert lat_long == (str(round(40.7360,2)), str(round(140.9560,2)))


def test_make_API_request(mocker):
    """Tests if the function makes an API request and return a tuple with temperatures and time"""
    latitude = str(round(59.9133,2))
    longitude = str(round(10.7389,2))
    mock_data = {'hourly':{'time': ['2024-11-14T00:00', '2024-11-14T01:00', '2024-11-14T02:00', '2024-11-14T03:00', '2024-11-14T04:00', '2024-11-14T05:00', '2024-11-14T06:00', '2024-11-14T07:00', '2024-11-14T08:00', '2024-11-14T09:00', '2024-11-14T10:00', '2024-11-14T11:00', '2024-11-14T12:00', '2024-11-14T13:00', '2024-11-14T14:00', '2024-11-14T15:00', '2024-11-14T16:00', '2024-11-14T17:00', '2024-11-14T18:00', '2024-11-14T19:00', '2024-11-14T20:00', '2024-11-14T21:00', '2024-11-14T22:00', '2024-11-14T23:00'], 'soil_temperature_0cm': [2.2, 1.8, 1.0, 0.5, 0.4, 0.6, 0.8, 1.0, 1.4, 1.8, 2.5, 3.5, 3.8, 2.8, 1.2, 0.1, -0.2, 0.0, 0.2, 0.5, 0.8, 1.0, 0.9, 0.7]}}
    mock_response = mocker.MagicMock()
    mock_response.json.return_value = mock_data
    mocker.patch("requests.get", return_value=mock_response)
    result = a_fun.make_API_request(latitude,longitude,'c')
    print(result)
    assert result == (mock_data['hourly']['soil_temperature_0cm'], mock_data['hourly']['time'])


def test_requested_temps():
    """Tests if the function returns a list with matching temperatures and time"""
    temp_list = [2.2, 1.8, 1.0, 0.5, 0.4, 0.6, 0.8, 1.0, 1.4, 1.8, 2.5, 3.5, 3.8, 2.8, 1.2, 0.1, -0.2, 0.0, 0.2, 0.5, 0.8, 1.0, 0.9, 0.7]
    temp_hours = ['2024-11-14T00:00', '2024-11-14T01:00', '2024-11-14T02:00', '2024-11-14T03:00', '2024-11-14T04:00', '2024-11-14T05:00', '2024-11-14T06:00', '2024-11-14T07:00', '2024-11-14T08:00', '2024-11-14T09:00', '2024-11-14T10:00', '2024-11-14T11:00', '2024-11-14T12:00', '2024-11-14T13:00', '2024-11-14T14:00', '2024-11-14T15:00', '2024-11-14T16:00', '2024-11-14T17:00', '2024-11-14T18:00', '2024-11-14T19:00', '2024-11-14T20:00', '2024-11-14T21:00', '2024-11-14T22:00', '2024-11-14T23:00']
    expected_result = ["-0.2 °C  at 16:00"]
    result = a_fun.requested_temps(temp_list, temp_hours, -0.1, 'below', 'c')
    assert result == expected_result


@patch('builtins.print')
def test_print_temps(mock_print):
    """Test if the function prints the matched temperatures"""
    temps = [" 2.0 °C  at 05:00", " 3.2 °C  at 06:00", " 4.7 °C  at 07:00", " 5.5 °C  at 08:00"]
    a_fun.print_temps(temps, 'Saint Petersburg', 5.7, 'below', 'C')
    mock_print.assert_called_with(" 5.5 °C  at 08:00")
    # Showing what is in mock
    sys.stdout.write(str( mock_print.call_args ) + '\n')
    sys.stdout.write(str( mock_print.call_args_list ) + '\n')
