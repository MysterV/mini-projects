import requests
parameters = {
    'amount': 10,
    'category': 12,  # music
    'type': 'boolean'
}
response = requests.get(f'https://opentdb.com/api.php', params=parameters)
response.raise_for_status()
question_data = response.json()['results']

