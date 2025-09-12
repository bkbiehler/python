import urllib.parse
import urllib.request
import json
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()
API_KEY = os.getenv("API_KEY")
LOCATION = "Kansas City, MO"
UNIT_GROUP = "metric"
CONTENT_TYPE = "json"

from dotenv import load_dotenv, dotenv_values

# Function to fetch timeline weather data
def fetch_timeline_weather():
    # Construct the request URL
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    request_url = f"{base_url}{urllib.parse.quote_plus(LOCATION)}?key={API_KEY}&unitGroup={UNIT_GROUP}&contentType={CONTENT_TYPE}"

    try:
        # Open the URL and read the response
        with urllib.request.urlopen(request_url) as response:
            if response.status != 200:
                print(f"Error: Received response status {response.status}")
                return
            # Decode the JSON response
            data = response.read().decode()
            weather_data = json.loads(data)

            # Process and print some parts of the response
            print(f"Weather forecast for {weather_data['resolvedAddress']}")
            for day in weather_data['days']:
                print(f"{day['datetime']}: {day['description']} - High: {day['tempmax']}C, Low: {day['tempmin']}C")
    except Exception as e:
        print(f"Error fetching weather data: {e}")

fetch_timeline_weather()