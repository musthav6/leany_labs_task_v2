import requests



class Weather:

    def __init__(self, api_key,base_url,lang="en"):
        self.base_url = base_url
        self.api_key = api_key
        self.lang = lang

    def get_weather(self, city):
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
            "lang":self.lang
        }
        try:
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                temperature = data["main"]["temp"]
                weather = data["weather"][0]["description"]

                return {
                    "temperature": temperature,
                    "weather": weather
                }
            return {"error": f"Error when get weather for the {city}. CODE: {response.status_code}"}
        except Exception as e:
            print(f"Error when get weather for the {city}: {e}")
            return {"error": "Error when get weather for the"}

