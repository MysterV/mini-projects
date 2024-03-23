log1 = {
    'Japan': {
        'visited': [],
        'visits': 0
        },
    'Germany': {
        'visited': ['Berlin', 'Hamburg', 'Stuttgart'],
        'visits': 2
        },
    'Poland': {
        'visited': ['Warsaw', 'Danzig', 'Krakow', 'Poznan', 'Radom', 'Lublin', 'Podlasie', 'Szczecin'],
        'visits': 1294
        },
}
for country in log1:
    print(country, log1[country]['visited'])


log2 = [
    {
        'country': 'Poland',
        'visited': ['Warsaw', 'Danzig', 'Krakow', 'Poznan', 'Radom', 'Lublin', 'Podlasie', 'Szczecin'],
        'visits': 1294
    },
    {
        'country': 'Germany',
        'visited': ['Berlin', 'Hamburg', 'Stuttgart'],
        'visits': 2
    },
    {
        'country': 'Japan',
        'visited': [],
        'visits': 0
    }
]

for i in range(len(log2)):
    print('\n\n', log2[i]['country'])
    print('visits:', log2[i]['visits'])
    print('places visited', log2[i]['visited'])

def add_country(country, visited=[], visits=0):
    new_country = {
        'country': country,
        'visited': visited,
        'visits': int(visits)
    }
    log2.append(new_country)

add_country('USA', ['New York', 'Washington'], 2)

for i in range(len(log2)):
    print('\n\n', log2[i]['country'])
    print('visits:', log2[i]['visits'])
    print('places visited', log2[i]['visited'])