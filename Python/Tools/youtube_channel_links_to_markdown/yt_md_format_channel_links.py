# User enters 1. YouTube channel @handle link and 2. channel ID, gets back 2 MD-formatted links to the channel in the form of
# [John](https://www.youtube.com/channel/UCqP87_SDfgerG43GASDvbDb) - [@john](https://www.youtube.com/@john)

import os
import bs4
import requests

# ===== CONFIG =====
template = '[{name}](https://www.youtube.com/channel/{id}) - [{handle}](https://www.youtube.com/{handle})'
handle = input('Channel handle (@name): ')
id = input('Channel ID: ')
output_file_path = 'output.txt'



# ===== CODE =====

# get name
site = requests.get(f'https://www.youtube.com/{handle}')
site.raise_for_status()
name = bs4.BeautifulSoup(site.text, 'html.parser').title.string.split(' - ')[0]


formatted = template.format(
    name=name,
    id=id,
    handle=handle)

with open(output_file_path, 'wt') as file:
    file.write(formatted)
    os.startfile(output_file_path)
