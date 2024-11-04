import csv
import requests

def get_db_cities() -> list:
    """
    Function that opens and reads the csv file that contains the world cities database.
    It returns a list of dictionaries, the cities.
    """
    worldcities = []
    try:
        with open('project/worldcities.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                worldcities.append(line)
        return worldcities
    except:
        print("Cannot open and read the csv file")


def search_city(city:str, country:str) -> list :
    """Searches matching cities in the list of world cities."""
    matching_cities = []
    worldcities = get_db_cities()
    for item in worldcities:
        try:
            if city.lower() in item['city'].lower() and country.lower() in item['country'].lower():
                matching_cities.append(item)
        except:
            return f"Cannot find {city} ({country}) in the database."
    if matching_cities:
        return matching_cities
    else:
        return None

def get_coords(selected_city : dict) -> tuple:
    """Get the coordinates of the selected city"""
    latitude = str(round(float(selected_city['lat']),2))
    longitude = str(round(float(selected_city['lng']),2))
    return (latitude,longitude)


def make_API_request(latitude:str, longitude:str, unit:str) -> tuple:
    """Request today's temperatures to the Open Meteo API."""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=soil_temperature_0cm&{unit}forecast_days=1"
    try:
        res = requests.get(url)
    except:
        return None
    data = res.json()
    temps = data['hourly']['soil_temperature_0cm']
    hours = data['hourly']['time']
    return (temps,hours)

    
def requested_temps(temp_list:list, temp_hours:list, user_temp:float, criteria:str, unit:str):
    """
    Check if today's temperatures are below/above the temperature entered by the user.
    This function returns a list with the matching hourly temperatures.
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

def print_temps(temp_list:list):
    """Print the temperatures and the hours in the console."""
    print("\nToday's temperatures are:\n")
    for t in temp_list:
        print(t)

if __name__ == "__main__":
    search_city(str,str)
    get_db_cities()
    get_coords(dict)
    make_API_request(str,str,str)
    requested_temps(list,list,float,str)
    print_temps(list)
