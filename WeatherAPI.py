# https://home.openweathermap.org/users/sign_in

import requests

def get_weather(city, api_key, units):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
    request = requests.get(url)
    content = request.json()
    print(content)

get_weather("Kannur", "7a1993517a8d4f46249b5e304a221083", 'standard')

