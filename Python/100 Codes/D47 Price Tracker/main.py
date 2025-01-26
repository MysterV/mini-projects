import requests
import lxml
from bs4 import BeautifulSoup

"""
A simple price checker, that is *supposed* to send you an email when the price meets your standards...
except I don't feel like creating an account to access an email sending API
so the code will just print the alert to a text file instead
"""

URL = 'https://www.amazon.pl/DayClocks-Klasyczny-zegar-dzienny-markerami/dp/B07NVSD3GH'
budget = 250
currency = 'zł'

# TODO:
# 1. Connect to the website
# 2. Scrape website's HTML and brew a Beautiful Soup
# 3. Find the product name and price tag
# 4. Compare the price to your budget
# 5. If the price is within budget, send an 'email' (aka write an alert to a text file)


# 1. Connect to the website
# Apparently every 2nd or 3rd request asks you to fill out a captcha, so the code will randomly break every few restarts
response = requests.get(url=URL, timeout=5.0, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-platform': 'Windows',
    'Accept-Language': 'en-US,en;q=0.9'})
response.raise_for_status()

# 2. Scrape website's HTML and brew a Beautiful Soup
soup = BeautifulSoup(response.text, 'lxml')

# 3. Find the product name and price tag
try:
    product = [i.get_text().strip() for i in soup.select_one('h1#title > span#productTitle')][0]
    price_tag = [i.get_text().strip() for i in soup.select('#corePriceDisplay_desktop_feature_div > div > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2) > span')]
    price = float(price_tag[0].strip(',')) + float(price_tag[1])/100
    price_currency = price_tag[2]
except:
    raise Exception('Amazon the bot, gave you a captcha, but the code cannot complete it.\nTry opening the URL in your browser and restarting the code, OR spam the restart button until it eventually runs.')
print(product)
print(price_tag)
print(price, price_currency)

# 4. Compare the price to your budget
# Don't bother with currency conversions
is_affordable = True if price <= budget and currency == price_currency else False
discount = round((budget - price)/budget*100, 1)
print(f'{is_affordable}, {-discount}%')

# 5. If the price is within budget, send an 'email' (aka write an alert to a text file)
if is_affordable:
    if price == budget:
        message = f'=====\n{product}\nThe product you are looking for is now the same price as your budget! That is: {price} {currency}'
    else:
        message = f'=====\n{product}\nThe product you are looking for is now {discount}% less than your budget! That is: {price} {currency}'
    try:
        with open('output.txt', 'xt', encoding='utf-8') as f: f.write(message)
    except FileExistsError:
        with open('output.txt', 'at', encoding='utf-8') as f: f.write('\n'+message)
