# **Data Integration from Multiple APIs**

## **1. API Analysis**

### **OpenWeatherMap API**
- **Endpoint:** `https://api.openweathermap.org/data/2.5/weather`
- **Parameters:**
    - `q`: City name
    - `appid`: API key
    - `units`: Measurement units ( We used  `metric` for Celsius)
    - `lang`: Response language (Depends on config value)
- **Response example:**
  ```json
  { "coord": {
       "lat": 40.7143, 
       "lon": -74.006},
    "main": {
      "temp": 6,
      "feels_like": 1,
      ...
  
  
    },
    "weather": [
      { "id": 100,
        "description": "clear sky",
        ...
      },
    "wind": {
      {
        "deg": 290, 
        "gust": 16.46, 
        "speed": 10.8}
  
      },
      
  ...
    ]
  }
  ```
- **Potential issues:**
    - API rate limits (60 requests per minute for free plan) - set sleep 1.1 sec
    - If city not found - get error message 

### **Wikipedia API**
- **Library used:** `wikipedia` Python module
- **Functionality:** Get summary of a city
- **Implementation:**
    - `wikipedia.summary(city, sentences=5)` get a 5 sentence description
- **Potential issues:**
    - City page might not exist - get error message
    - Disambiguation error (multiple results found) - then we get firs page

---

## **2. Data Retrieval and Integration**

1. **List of cities:**
    - This list defined in config.py
   ```python
   CITIES = ["New York", "Tokyo", "São Paulo"]
   ```
   - We can send any other list with cities
   
   ```python
   def main(city_list=None):
   ```
    
2. **Fetching weather data**
    - Requests data from OpenWeatherMap API
    - Get temperature and weather description
3. **Fetching city descriptions**
    - Uses Wikipedia API to get a summary for the city
4. **Combining data**
    - Data is structured as:
      ```json
      {
        "city": "New York",
        "temperature": 22.5,
        "weather": "clear sky",
        "description": "New York is the most populous city in the United States."
      }
      ```

---

## **3. Python Script Overview**

### **Files Structure**
- `main.py` → Orchestrates data retrieval and processing
- `weather.py` → Handles OpenWeatherMap API requests
- `wiki.py` → Fetches city descriptions from Wikipedia
- `config.py` → Stores configuration variables (API key, city list, base URL)

### **Code examples**
#### **Fetching Weather Data**
```python
response = requests.get(self.base_url, params=params)
if response.status_code == 200:
    data = response.json()
    return {
        "temperature": data["main"]["temp"],
        "weather": data["weather"][0]["description"]
    }
```

#### **Fetching Wikipedia Data**
```python
try:
    return wikipedia.summary(city, sentences=5)
except wikipedia.exceptions.DisambiguationError as e:
    best_match = e.options[0]
    return wikipedia.summary(best_match, sentences=5)
```

---

## **5.Improvements**

### **Potential Improvements**
- **Asynchronous requests** using `asyncio` + `aiohttp` for better performance
- **Saving results in DB or cashing it** to avoid unnecessary API calls
- **Logging**
- **Checking if API_KEY** is valid
- **Save cities in DB** with possibility to add new city
