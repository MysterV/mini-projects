# User enters a YouTube channel link, gets back 2 MD-formatted links to the channel in the form of
# [John](https://www.youtube.com/channel/UCqP87_SDfgerG43GASDvbDb) - [@john](https://www.youtube.com/@john)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import re
import os

# ===== CONFIG =====
# template supports {name}, {handle}, {id}, {url_id}, {url_handle}
TEMPLATE = '[{name}]({url_id}) - [{handle}]({url_handle})'
OUTPUT_FILE_PATH = 'output.txt'
CHANNEL_URLS = [input('URL: ')]


# ===== CODE =====
# Selenium stuff
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")


def fetch_channel_data(url, driver) -> dict:
    driver.get(url)
    time.sleep(1)
    # Cookies consent page
    try:
        reject_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Reject all"]')
        reject_button.click()
        print("Clicked reject cookies button.")
        time.sleep(1)
    except:
        print("Reject cookies button not found or already rejected.")


    # Full page - the real deal
    print('YouTube loaded. Extracting channel name, ID, @handle and URLs...')
    html = driver.page_source

    name = re.search(r'<meta itemprop="name" content="([^"]+)', html).group(1)
    url_id = re.search(r'"channelUrl"\s*:\s*"(https://www.youtube.com/channel/[\w-]+)"', html).group(1)
    url_handle = re.search(r'"vanityChannelUrl"\s*:\s*"(http://www.youtube.com/@[^"]+)', html).group(1).replace('http://', 'https://')
    channel_id = url_id.split('channel/')[1]
    handle = url_handle.split('.com/')[1]
    return {
        'name': name,
        'handle': handle,
        'channel_id': channel_id,
        'url_id': url_id,
        'url_handle': url_handle
    }


def format_data(template: str, data: dict) -> str:
    return template.format(
            name=data['name'],
            handle=data['handle'],
            id=data['channel_id'],
            url_id=data['url_id'],
            url_handle=data['url_handle'])


def md_format(urls: list):
    driver = webdriver.Chrome(options=options)
    with open(OUTPUT_FILE_PATH, 'wt') as file:
        for url in urls:
            data = fetch_channel_data(url, driver)
            formatted = format_data(TEMPLATE, data)
            file.write(formatted + '\n')
    driver.quit()


# Fill in the template and output
if CHANNEL_URLS:
    md_format(CHANNEL_URLS)
    os.startfile(OUTPUT_FILE_PATH)
else:
    print('No URL provided.')

print('Done!')
