# use example

import path_to_uri as ptu

addresses = {
    'file://': '/',
    'http://': 'localhost:8080/'
}

while True:
    path = input('Path to encode (leave empty to exit):\n')
    if not path:
        break
    for protocol, address in addresses.items():
        print(ptu.to_uri(path=path, protocol=protocol, address=address))