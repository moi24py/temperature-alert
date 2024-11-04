import user_funcs as u_fun
import app_funcs as a_fun
import email_funcs as e_fun

city,country,temperature,unit,criteria = u_fun.user_inputs()

matched_cities = a_fun.search_city(city,country)

if not matched_cities:
    print(
        f'''
        Cannot find {city.capitalize()} ({country.capitalize()}) in the database.
        It is not in the database, or it may have a different spelling.
        Please, try again or enter a city nearby.
        ''')
else:
    if len(matched_cities) > 1:
        selected_city = u_fun.choose_city(matched_cities)
        if selected_city:
            city = selected_city['city']
            country = selected_city['country']
            latitude, longitude = a_fun.get_coords(selected_city)
        else:
            print("You have not selected a city.")
    else:
        latitude, longitude = a_fun.get_coords(matched_cities[0])

    weather_data = a_fun.make_API_request(latitude,longitude,unit[1])

    if weather_data:
            temps,hours = weather_data
            matched_temps = a_fun.requested_temps(temps,hours,temperature,criteria,unit[0])
            if not matched_temps:
                print(f"{city.capitalize()} temperatures today are not {criteria} {temperature}°{unit[0].upper()}")
                exit()
            # if there is at least one temperature that matches the condition
            # ask the user if they want it to be printed or sent as an email
            pref = u_fun.print_or_send()
            if pref == 'p':
                a_fun.print_temps(matched_temps)
            if pref == 's':
                e_fun.send_email(city, temps, hours, temperature, unit[0], criteria)
    else:
        print("Cannot retrieve weather data.")
