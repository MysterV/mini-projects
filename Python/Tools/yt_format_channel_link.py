import os
import bs4
import requests as re

# User enters 1. channel @handle link and 2. channel ID, gets 2 MD-formatted links to the channel in the form of:
template = '[{channel_name}](https://www.youtube.com/channel/{id}) - [{handle}]({url_handle})'
# e.g. [John](https://www.youtube.com/channel/UCqP87_SDfgerG43GASDvbDb) - [@john](https://www.youtube.com/@john)


output_file_path = 'output.txt'
url_handle = input('handle URL: ')
handle = url_handle.split('.com/')[1]
id = input('Channel ID: ')

site = re.get(url_handle)
site.raise_for_status()
channel_name = bs4.BeautifulSoup(site.text, 'html.parser').title.string.split(' - ')[0]

message = template.format(
    channel_name=channel_name,
    id=id,
    handle=handle,
    url_handle=url_handle)

with open(output_file_path, 'wt') as file:
    file.write(message)
    os.startfile(output_file_path)
