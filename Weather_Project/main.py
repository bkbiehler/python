import urllib.parse
import urllib.request
import json
import os
import sys
from dotenv import load_dotenv, dotenv_values

load_dotenv()
# Load API key from .env file
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    print("Error: API_KEY environment variable is not set.")
    sys.exit(1)


# Function to prompt user for location
def loc_prompt(location):
    return input(location)

print("Starting program.")
l=loc_prompt("Insert Location: ")
print(l)
UNIT_GROUP = "us"
CONTENT_TYPE = "json"

# Function to fetch timeline weather data
def fetch_timeline_weather(l):
    # Construct the request URL
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    request_url = f"{base_url}{urllib.parse.quote_plus(l)}?key={API_KEY}&unitGroup={UNIT_GROUP}&contentType={CONTENT_TYPE}"

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

fetch_timeline_weather(l)
