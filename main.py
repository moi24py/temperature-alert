import modules.user_funcs as u_fun
import modules.app_funcs as a_fun
import modules.email_funcs as e_fun

# Ask for city and country to the user
city = u_fun.get_loc('city')
country = u_fun.get_loc('country')

# Find the city in the database
matched_cities = a_fun.search_city(city,country)

# If there is no city in the databse print a message and exit the program
if not matched_cities:
    print(
        f'''
        Cannot find {city.capitalize()} ({country.capitalize()}) in the database.
        It is not in the database, or it may have a different spelling.
        Please, try again or enter a city nearby.
        ''')
    exit()

# If there are multiple results
if len(matched_cities) > 1:
    # Ask the user to choose one
    selected_city = u_fun.choose_city(matched_cities)
    # If the user selected a city gets the city's coordinates
    if selected_city:
        city = selected_city['city']
        country = selected_city['country']
        latitude, longitude = a_fun.get_coords(selected_city)
    else:
        print("You have not selected a city.")
# If there is only one result
else:
    city = (matched_cities[0]['city'])
    country = (matched_cities[0]['country'])
    print(f"{city} in {country}")
    # get the city's latitude and longitude
    latitude, longitude = a_fun.get_coords(matched_cities[0])

temperature,unit,criteria = u_fun.user_inputs()
criteria = criteria.lower()

# Make the API request to get the city's weather
weather_data = a_fun.make_API_request(latitude,longitude,unit[1])

# If the request was not successful
if not weather_data:
    # print a message and exit the program
    print("Sorry, cannot retrieve weather data. Exiting now.")
    exit()

# If the API request was successful
# get the today's hourly temperatures
temps,hours = weather_data
# check if there are temperatures that corrisponds to the range entered by the user 
matched_temps = a_fun.requested_temps(temps,hours,temperature,criteria,unit[0])
# if there aren't matching temperatures
if not matched_temps:
    # print a message and exit the program
    print(f"{city.capitalize()} temperatures today are not {criteria} {temperature}°{unit[0].upper()}")
    exit()
   
# If there are matching temperatures
# ask the user if they want the list to be printed or sent as an email
pref = u_fun.print_or_send()
# print
if pref == 'p':
    a_fun.print_temps(matched_temps, city, temperature, criteria, unit[0].upper())
# send
if pref == 's':
    e_fun.send_email(city, matched_temps, temperature, unit[0].upper(), criteria)
