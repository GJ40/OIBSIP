import requests

api_key = open("api_key.txt", 'r').read()

city_name = input("Enter city: ")

response = requests.get(
    f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city_name}"
)

weather_data = response.json()
#print(weather_data)

temperature_K = str(weather_data['main']['temp']) + "K"
temperature_C = str(float(weather_data['main']['temp']) - 272.15)[0:5] + "C"
humidity = str(weather_data['main']['humidity']) + "%"
wind = str(weather_data['wind']['speed']) + " km/h"
weather = str(weather_data['weather'][0]['main'])
weather_condition = str(weather_data['weather'][0]['description'])

print("Temperature: ", temperature_K, "\n\t\t\t  " + temperature_C)
print("Humidity: ", humidity)
print("Wind: ", wind)
print("Weather: ", weather, "\nWeather_Condition: ", weather_condition)
