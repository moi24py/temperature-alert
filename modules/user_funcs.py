import regex as re

# Pattern for city and country validation.
# [-(\p{L}’‘\'./234)\p{M}* .,]{3,50}$
city_country_regex = re.compile(r'^[-(\p{L}’‘\'./)\p{M}* .,]{3,50}[234]{0,3}$', re.I)

# Pattern for temperature validation.
temp_regex = re.compile(r'^[-+]?[0-9]{1,3}(\.[0-9])?$')

# Pattern for criteria validation.
criteria_regex = re.compile(r'^[a,b,e,l,o,v,w]{5}$', re.I)

def get_loc(location : str) -> str:
    """Persistently ask the user for a name (city or country)."""
    i = 0
    while i < 4:
        user_loc = input(f"Please, enter a {location} (at least 3 letters): ")
        try:
            match = city_country_regex.fullmatch(user_loc)
            if match:
                return match.group()
            else:
                raise TypeError("Invalid input, one or more invalid characters were used.")
        except:
            print("Try again. Please only use letters, space, hyphen and comma.")
            i += 1
    raise TypeError("Invalid input, one or more invalid characters were used.")


def get_temp() -> float:
    """Persistently ask the user for a temperature."""
    i = 0
    while i < 4:
        user_temp = input(f"Please, enter a temperature: ")
        try:
            match = temp_regex.fullmatch(user_temp)
            if match:
                return float(match.group())
            else:
                raise TypeError("Invalid input, one or more invalid characters were used. End of program.")
        except:
            i += 1
            print("Please, only use an integer (e.g. \"30\"), or a decimal with one decimal place (e.g. \"30.2\").")
    raise TypeError("Invalid input, one or more invalid characters were used. End of program.")

def get_criteria(temp : float, unit : str) -> str:
    """
    Persistently ask the user what temperatures they are interested in:
    below or above the given temperature.
    """
    i = 0
    while i < 4:
        user_crit = input(f"Are you interested in knowing temperatures below or above {temp}°{unit.upper()}? (below/above): ")
        try:
            match = criteria_regex.fullmatch(user_crit)
            if match:
                return match.group()
            else:
                raise TypeError("Invalid input, one or more invalid characters were used. End of program.")
        except:
            i += 1
            print("Please, try again. The only accepted values are: \"above\" and \"below\".")
    raise TypeError("Invalid input, one or more invalid characters were used. End of program.")

# Celsius or Fahrenheit
def temp_unit() -> tuple:
    """Persistenly ask the user for a temperature unit: Celsius or Fahrenheit."""
    i = 0
    while i < 4:
        user_unit = input("Enter \"c\" for Celsius, \"f\" for Fahrenheit: ")
        if user_unit.lower() == 'f':
            unit_url_param = "temperature_unit=fahrenheit&"
            return (user_unit, unit_url_param)
        if user_unit.lower() == 'c':
            unit_url_param = ''
            return (user_unit, unit_url_param)
        else:
            i += 1
            print("Please, enter c or f. Try again.")
    raise ValueError("Invalid input. Maximum attempts reached. End of program.")

def user_inputs() -> tuple:
    """
    Ask the user for city, country, temperature, Celsius/Fahrenheit.
    The function returns a tuple.
    """
    city = get_loc('city')
    country = get_loc('country')
    temperature = get_temp()
    unit_C_F = temp_unit()
    criteria = get_criteria(temperature, unit_C_F[0])
    user_data = (city,country,temperature, unit_C_F, criteria)
    return user_data

def choose_city(matched_cities : list) -> dict:
    """
    If there is more than one city with that name, ask the user which one they prefer.
    The function returns a dictionary of the selected city.
    """
    choices_qty = len(matched_cities)
    item_num = 0
    print("Multiple results found:")
    try:
        for item in matched_cities:
            print(f" ({item_num}) : {item['city']} in {item['country']}")
            item_num += 1
    except:
        return None
    i = 0
    while i < 4:
        index_str = input("Please enter the number that corrisponds to the desired city: ")
        try:
            index_num = int(index_str)
        except:
            i += 1
            print(f"Please, only insert numbers.")
        try:
            return matched_cities[index_num]
        except:
            i += 1
            print(f"Only numbers from 0 to {choices_qty-1} are accepted.")
    raise TypeError("Invalid input. Maximum attempts reached. End of program.")

def print_or_send():
    """Persistently ask the user if they want the results to be printed or sent as an email."""
    i = 0
    while i < 4:
        pref = input("Do you prefer the results to be printed in the console or sent as an email? (p/s): ")
        if pref == 'p':
            return 'p'
        if pref == 's':
            return 's'
        else:
            i += 1
            print("Please enter: \"p\" for printing or \"s\" for sending.")
    raise TypeError("Invalid input. Maximum attempts reached. End of program.")

if __name__ == "__main__":
    get_loc('city or country')
    get_temp()
    temp_unit()
    get_criteria(18.0,'c')
    user_inputs()
    choose_city(['Los Angeles'])
    print_or_send()
