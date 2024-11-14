import csv
import requests

path = 'modules/worldcities.csv'

def get_db_cities(path : str) -> list[dict]:
    """
    Opens and reads the csv file that contains the world cities database.

    Parameters
    ----------
    str
        A string with the path of the 'worldcities.csv' file
    
    Returns
    -------
    list
        a list of dictionaries representing the cities.
    """
    if not os.path.isfile(path):
        print("There is no 'worldcities.csv' file in this directory")
        raise FileNotFoundError(f"File '{path}' not found.")
    
    worldcities = []
    try:
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                worldcities.append(line)
        return worldcities
    except Exception as e:
        print(f"Cannot open and read the csv file: {e}")
        return None
        

def search_city(city:str, country:str) -> list[dict] :
    """
    Searches matching cities in the list of world cities.
    
    Parameters
    ----------
    city : str
        The city's name to search in the database
    country : str
        The name of the country in which the city is located

    Returns
    -------
    list
        a list of dictionaries representing the matching city/cities
    """
    matching_cities = []
    worldcities = get_db_cities()
    if worldcities:
        for item in worldcities:
            try:
                if city.lower() in item['city'].lower() and country.lower() in item['country'].lower():
                    matching_cities.append(item)
            except:
                return f"Cannot find {city} ({country}) in the database."
    else:
        print("Cannot search in the database.")
        exit()
    if matching_cities:
        return matching_cities
    else:
        return None

def get_coords(selected_city:dict) -> tuple:
    """
    Gets the coordinates of the selected city.
    
    Parameters
    ----------
    selected_city : dict
        The city selected by the user

    Returns
    ------
    tuple
        A tuple containing two strings, the city's latitude and longitude.
    """
    latitude = str(round(float(selected_city['lat']),2))
    longitude = str(round(float(selected_city['lng']),2))
    return (latitude,longitude)

def make_API_request(latitude:str, longitude:str, unit:str) -> tuple:
    """
    Requests today's temperatures to the Open Meteo API.
    
    Parameters
    ----------
    latitude : str
        The string that represents the city's latitude
    longitude : str
        The string that represents the city's longitude
    unit : str
        The string that represents the temperature unit 

    Returns
    -------
    tuple
        a tuple of lists representing temperatures (floats) and hours (strings)
    """
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=soil_temperature_0cm&{unit}forecast_days=1"
    try:
        res = requests.get(url)
    except:
        return None
    
    data = res.json()
    temps = data['hourly']['soil_temperature_0cm']
    hours = data['hourly']['time']
    
    return (temps,hours)

def requested_temps(temp_list:list[float], temp_hours:list[str], user_temp:float, criteria:str, unit:str) -> list[str]:
    """
    Checks if today's temperatures are below/above the temperature entered by the user.

    Parameters
    ----------
    temp_list : list[float]
        A list of floats representing the temperatures
    temp_hours : list[str]
        A list of strings representing the hours
    user_temp : float
        A float representing the temperature entered by the user
    criteria : str
        A string representing the criteria ('below'/'above') entered by the user
    unit : str
        The string that represents the temperature unit

    Returns
    -------
    list[str]
        a list of strings representing the matched hourly temperatures.
    """
    matched_temps = []
    for i in range(len(temp_list)):
        if criteria == 'above':
            cond = temp_list[i] > user_temp
        else:
            cond = temp_list[i] < user_temp
        if cond:
            # if the decimal has only 1 unit, add a space to make it even
            if len(str(temp_list[i])) == 3:
                space = " "
            else:
                space = ""
            matched_temps.append(f"{space}{temp_list[i]} °{unit.upper()}  at {temp_hours[i].split('T')[1]}")
    return matched_temps

def print_temps(temp_list : list[str], city : str, user_temp : float, criteria : str, unit: str):
    """
    Prints the temperatures and the hours in the console.
    
    Parameters
    ----------
    temp_list : list[str]
        A list of strings representing the matched temperatures
    city : str
        The name of the city found in the database
    user_temp:float
        A float representing the temperature entered by the user
    criteria : str
        A string representing the criteria ('below'/'above') entered by the user
    unit : str
        The string that represents the temperature unit
    """
    print(f"\n{city} today temperatures that are {criteria} {user_temp}°{unit}:\n")
    for t in temp_list:
        print(t)


if __name__ == "__main__":
    search_city('Venice','Italy')
    get_db_cities()
    get_coords({'lat': 45.44,'lng': 12.21})
    make_API_request('45.44','12.21','')
    requested_temps([9.8,10.4,15.8,19.7,23.4],["10:00","11:00","12:00","13:00","14:00", 15.0,'above','c'], 18.0, 'above', 'c')
    print_temps([9.8,10.4,15.8,19.7,23.4], 'Venice', 18.0, 'above', 'c')
