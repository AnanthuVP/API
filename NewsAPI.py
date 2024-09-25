

import requests

def get_news(from_date, to_date, api_key):
    url = f"https://newsapi.org/v2/everything?qInTitle=stock%20market&from={from_date}&to={to_date}&sortBy=popularity&language=en&apiKey={api_key}"
    request = requests.get(url)
    content = request.json()
    print(content)

get_news(from_date=2024-05-07, to_date=2024-05-08, api_key=)