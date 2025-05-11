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
CHANNEL_URL = input('URL: ')



# ===== CODE =====
# Selenium stuff
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=options)


# Cookies consent page
driver.get(CHANNEL_URL)
time.sleep(1)
try:
    reject_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Reject all"]')
    reject_button.click()
    print("Clicked reject cookies button.")
    time.sleep(1)
except:
    print("Reject cookies button not found or already rejected.")


# Full page - the real deal
print('YouTube loaded. Extracting channel ID and @handle...')
html = driver.page_source

# Close the browser
driver.quit()

# Read all the data
url_id = re.search(r'"channelUrl"\s*:\s*"(https://www.youtube.com/channel/[\w-]+)"', html).group(1)
url_handle = re.search(r'"vanityChannelUrl"\s*:\s*"(http://www.youtube.com/@[^"]+)', html).group(1)
channel_id = url_id.split('channel/')[1]
handle = url_handle.split('.com/')[1]
name = re.search(r'<meta itemprop="name" content="([^"]+)', html).group(1)

# Fill in the template
formatted = TEMPLATE.format(
    name=name,
    handle=handle,
    id=channel_id,
    url_id=url_id,
    url_handle=url_handle)

# Output result
with open(OUTPUT_FILE_PATH, 'wt') as file:
    file.write(formatted)
    os.startfile(OUTPUT_FILE_PATH)
print('Done!')
