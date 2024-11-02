# Module for user functions.

import regex as re

# Pattern for city and country validation.
city_country_regex = re.compile(r'^[-(\p{L}’‘\'./)\p{M}* .,]{3,50}[234]{0,3}$', re.I)

# Pattern for temperature validation.
temp_regex = re.compile(r'^[-+]?[0-9]{1,3}(\.[0-9])?$')

# Pattern for criteria validation.
criteria_regex = re.compile(r'^[a,b,e,l,o,v,w]{5}$', re.I)

def get_loc(location : str) -> str:
    """Persistently ask the user for a name (city or country)."""
    while True:
        user_loc = input(f"Please, enter a {location} (at least 3 letters): ")
        try:
            match = city_country_regex.fullmatch(user_loc)
            if match:
                return match.group()
            else:
                raise TypeError("Invalid input, one or more invalid characters were used.")
        except:
            print("Try again. Please only use letters, space, hyphen and comma.")
