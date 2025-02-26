import requests

api_key = "5b16b0cedae2f3103972f9bde11f80da"  # Replace if invalid
weather_url = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")

params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}

try:
    response = requests.get(weather_url, params=params)
    if response.status_code != 200:  # Check if it failed
        print(f"Oops! Problem with the request. Error code: {response.status_code}")
        if response.status_code == 401:
            print("API key might be wrong!")
        elif response.status_code == 404:
            print("City not found!")
        exit()

    weather_data = response.json()

    temp = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    condition = weather_data["weather"][0]["description"]

    print(f"Weather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition}")

except requests.exceptions.RequestException:
    print("Oops! No internet or something broke.")