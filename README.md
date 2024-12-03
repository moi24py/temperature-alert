# temperature-alert

This is my first program! :)
It's a personal project. It checks if today's hourly temperatures are above or below a given temperature. You can run it in the console. If you prefer, an email with the retrieved data can be sent to the specified recipients; in this case, you need a Google account.

## Table of Contents
- [Why & How](#why--how)
- [Installation](#installation)
- [Usage](#usage)
- [Bugs](#bugs)
- [Lesson Learned](#lessons-learned)
- [Resources](#resources)

## Why & How:

:turtle: My tortoise lives in the garden and needs shelter when the temperatures are below 4°C. He always acts like a tough guy who doesn't need protection, but he does indeed. If the weather is cold, I put him in his house - if he's not already there.

Before learning Python, I had to check the weather manually every day. After learning Python, I automated this process by making a simple app that checks daily if and when the temperatures in my city are below 4°C and sends me an email.

A couple of weeks later, I thought that maybe some other people have a similar need. So, I began expanding the idea behind the app to make it customizable. That's how "temperature-alert" was born.

To make this app I used Python with a dash of HTML and CSS.


## Installation
1. Clone the repository:
```bash
 git clone https://github.com/moi24py/temp-alert.git
```

2. Install dependencies:
```bash
 pip install requirements.txt
 ```


## Usage

### Run
To run the app, go to the app directory via Terminal, and enter:
```
temp-alert % Python3 main.py
```

### How does it work
A few questions will be prompted and, depending on your answers, you'll get a different output.

First, you will be asked to type the city you are interested in and its country. The spelling is case insesitive and it's not important to type complete names.

example a)
```
Please, enter a city (at least 3 letters): Novosibirsk
Please, enter a country (at least 3 letters): Russia
```
example b)
```
Please, enter a city (at least 3 letters): lisb
Please, enter a country (at least 3 letters): port
```

In the database [(credits: simplemaps.com)](https://simplemaps.com/data/world-cities), some city and country names are separated with commas or hyphens.
Only enter the word that best identifies the city/country, without "The", "South", "-", etc.

You can also type these countries with their complete names, but please make sure they are spelled accordingly:

- Virgin Islands, British
- Micronesia, Federated States of
- Gambia, The
- Bonaire, Sint Eustatius, and Saba
- Saint Helena, Ascension, and Tristan da Cunha
- Korea, South
- Bahamas, The
- Korea, North
- Timor-Leste
- Guinea-Bissau

The program will search in the database to find the requested city. If the database cannot be found, it will raise an error. If the database is found, the search will start.
If there is one matching city, it will print the name of the city and its country.

example a)
```
Novosibirsk in Russia
```
example b)
```
Lisbon in Portugal
```

If multiple cities are found, the app will ask you to choose from the provided list by entering the corresponding number:
```
Please, enter a city (at least 3 letters): Ban S
Please, enter a country (at least 3 letters): Thailand
Multiple results found:
 (0) : Ban Suan in Thailand
 (1) : Muban Saeng Bua Thong in Thailand
 (2) : Ban Sai Ma Tai in Thailand
 (3) : Ban Song in Thailand
 (4) : Ban Samo Khae in Thailand
 (5) : Ban San Phak Wan Luang in Thailand
 (6) : Ban Sop Tia in Thailand
 (7) : Ban Saeo in Thailand
 (8) : Ban Sathan in Thailand
 (9) : Ban San Pong in Thailand
 (10) : Ban Son Loi in Thailand
 (11) : Ban Si Don Chai in Thailand
 (12) : Ban Sai Yoi in Thailand
Please enter the number that corrisponds to the desired city: 5
Ban San Phak Wan Luang in Thailand
```

If no city is found, it prints a message to let you know, and the program stops.
```
Please, enter a city (at least 3 letters): aeiou
Please, enter a country (at least 3 letters): ouiea

        Cannot find Aeiou (Ouiea) in the database.
        It is not in the database, or it may have a different spelling.
        Please, try again or enter a city nearby.
```

When a city is found, the app asks for the temperature. You can enter an integer or float.
```
Please, enter a temperature: -2.3
```

If the temperature is in Celsius or Fahrenheint. Only "c" and "f" are allowed.
```
Enter "c" for Celsius, "f" for Fahrenheit: c
```

Than, the app will ask whether the interesting range of temperatures is below or above the given temperature.
Please note that the only words allowed are "above" and "below" (case insensitive) spelled exactly like that. Letters not contained in the aforementioned words, spaces, quotes, commas, numbers, or any other character, are not allowed. The user will be continuously prompted by the function to select the appropriate choice between "below" and "above".
```
Are you interested in knowing temperatures below or above -2.3°C?(below/above): below
```

example: a space before the word
```
Are you interested in knowing temperatures below or above 12.3? (below/above):  above
Please, try again. The only accepted values are: "above" and "below".
```

example: a quoted word
```
Are you interested in knowing temperatures below or above 12.3? (below/above): "below"    
Please, try again. The only accepted values are: "above" and "below".
```

An API request is made to get the city weather, if it is not successful it raises an error and exits the program.
```
Sorry, cannot retrieve weather data. Exiting now.
```

If the call is successful, temperatures and times are extracted.

Case 1)

If there are temperatures below/above the requested temperature, the program will ask if you want them to be printed or sent as an email.
1.1) Example with printed:
```
temp-alert % Python3 main.py
    
Please, enter a city (at least 3 letters): Novosibirsk
Please, enter a country (at least 3 letters): Russia
Novosibirsk in Russia
Please, enter a temperature: -2.3
Enter "c" for Celsius, "f" for Fahrenheit: c
Are you interested in knowing temperatures below or above -2.3°C?(below/above): below
Do you prefer the results to be printed in the console or sent as anemail? (p/s): p

Novosibirsk today temperatures that are below -2.3°C:

-2.4 °C  at 15:00
-2.6 °C  at 16:00
-2.6 °C  at 17:00
-2.8 °C  at 18:00
-2.9 °C  at 19:00
-3.1 °C  at 20:00
-3.2 °C  at 21:00
-3.3 °C  at 22:00
-3.4 °C  at 23:00
```

1.2) Example with send:

```
temp-alert % Python3 main.py
    
Please, enter a city (at least 3 letters): Novosibirsk
Please, enter a country (at least 3 letters): Russia
Novosibirsk in Russia
Please, enter a temperature: -2.3
Enter "c" for Celsius, "f" for Fahrenheit: c
Are you interested in knowing temperatures below or above -2.3°C?(below/above): below
Do you prefer the results to be printed in the console or sent as anemail? (p/s): s
```
![email example](https://github.com/user-attachments/assets/78c80734-eaa9-4e30-9a4e-068a9bc8930b)

To send emails, please generate an App Password ([Google guide](https://support.google.com/mail/answer/185833?hl=en)) and fill out the blank variables ```sender```, ```contacts```, ```msg['From']```, ```password``` in ```modules/email_funcs.py```:

```
# myemail@gmail.com
sender = ""

# e.g. ["contact1@yahoo.com", "contact2@gmail.com"]
contacts = []
    
# my name
msg['From'] = ""

# App password generated via Google Account
password = ""
```

Here is an example:
```
sender = "mybestemail@gmail.com"

contacts = ["1234@yahoo.com", "5678@domain.net"]

msg['From'] = "Me myself and I"

password = "abcdefghijklmnop"
```

Case 2)

If the temperatures are not below or above the temperature you entered, a message will be printed in the console to let you know.

Example:
```
temp-alert % Python3 main.py

Please, enter a city (at least 3 letters): Sydney
Please, enter a country (at least 3 letters): Australia
Sydney in Australia
Please, enter a temperature: 65
Enter "c" for Celsius, "f" for Fahrenheit: f
Are you interested in knowing temperatures below or above 65.0°F?(below/above): below
Sydney temperatures today are not below 65.0°F
```

## Bugs
Found a bug? Please, let me know at moi24py@gmail.com


## Lessons Learned
I learned a lot thanks to this project!
In general:
- Before writing code: have a precise idea of what the project will be, its purpose, and its usage.
- When writing code: organize the code into small units and always choose "simple and clear" over "concise and cryptic". Refactor the code when possible. Test the code and write docstrings while developing.
- After writing the code: write the docs.

Specifically, I learned the basics of how to:
- Send emails
- Use jinja2, pytest and unittest
- Test the code
- Write the docs

## Resources
Thanks to these resources I was able to learn new skills and make this app work.

* Official docs of Python and the modules I used.
* [realpython.com](https://realpython.com/)
* [pytest-with-eric.com](https://pytest-with-eric.com/)
* [mailtrap.io/blog](https://mailtrap.io/blog/)
* [freecodecamp.com](https://www.freecodecamp.org/)
* [medium.com](https://medium.com/)
