import requests
import datetime as dt

me_lat = 84.503
me_lng = 0.3142

# ----- Find the ISS -----
response_iss = requests.get("http://api.open-notify.org/iss-now.json")
response_iss.raise_for_status()
iss_pos = response_iss.json()['iss_position']
print('The ISS is located at:', iss_pos['latitude'], iss_pos['longitude'])


# ----- Find out if you're close enough to see the ISS -----
def is_close_enough():
    if me_lat-5 < float(iss_pos['latitude']) < me_lat+5 and me_lng-5 < float(iss_pos['longitude']) < me_lng+5:
        return True


# ----- Find out if it's dark enough outside to see the ISS -----
parameters = {
    'lat': me_lat,
    'lng': me_lng,
    'formatted': 0
}

response_sunrise = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response_sunrise.raise_for_status()
suntime = response_sunrise.json()['results']
sunrise = suntime['sunrise'].split('T')[1].split(':')[0]
sunset = suntime['sunset'].split('T')[1].split(':')[0]

print(f'sunrise: {sunrise}, sunset: {sunset}')

time = dt.datetime.now()
def is_dark_enough():
    if time.hour < sunrise or time.hour > sunset:
        return True

if is_close_enough() and is_dark_enough():
    print('Go touch some grass and look in the sky.')
else:
    print('Nothing to see here.')
