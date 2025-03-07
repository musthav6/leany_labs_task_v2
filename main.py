import json
import time

from weather import Weather
from wiki import Wiki

from config import BASE_LANGUAGE, API_KEY,BASE_URL,CITIES # отримуємо ключ, мову, міста та урлу з конфіга

def main(city_list=None):
    weather_api = Weather(API_KEY,BASE_URL,lang=BASE_LANGUAGE) # ініціалізація класів для роботи з апішками
    wiki_api = Wiki(lang=BASE_LANGUAGE)

    if city_list is None:
        city_list = CITIES
    results = []

    for city in city_list:
        time.sleep(1.1) # передбачаємо ліміт в опенвезері 60 запитів на хвилину


        weather = weather_api.get_weather(city)
        description = wiki_api.get_city_description(city)

        result = {
            "city": city,
            "temperature": weather.get("temperature",f'Data not available for {city}'),
            "weather": weather.get('weather',f'Data not available for this {city}'),
            "description": description
        }
        print(result)
        results.append(result)




if __name__ == "__main__":
    main()
