import requests

api_key = None
my_data = {
    'lat': -82.862755,
    'lon': 135.0,
    'appid': api_key,
    'exclude': 'current,minutely,daily'
}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall')
response.raise_for_status()
print(response)
data = response.json()['hourly']

is_going_to_rain = False
for i in data:
    if data[i]['weather'][0][main] == 'Rain':
        is_going_to_rain = True
        break

print('Rain is coming!')

