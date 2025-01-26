from selenium import webdriver
from selenium.webdriver.common.by import By
import time

weeb = webdriver.Edge()
weeb_conf = webdriver.EdgeOptions()
weeb_conf.add_experimental_option('detach', True)


weeb.get('https://orteil.dashnet.org/cookieclicker/')
# select language
language_select = None
while not language_select:
    try:
        language_select = weeb.find_element(By.CSS_SELECTOR, 'div#langSelect-EN')
        language_select.click()
    except:
        pass
time.sleep(1)

# find cookie and basic upgrades
cookie = weeb.find_element(By.CSS_SELECTOR, 'button#bigCookie')
# golden_cookie = weeb.find_element(By.CSS_SELECTOR, 'button.shimmer')
cursors = weeb.find_element(By.CSS_SELECTOR, 'div#product0')
cursors_owned = weeb.find_element(By.CSS_SELECTOR, 'div#productOwned0')
grandmas = weeb.find_element(By.CSS_SELECTOR, 'div#product1')
grandmas_owned = weeb.find_element(By.CSS_SELECTOR, 'div#productOwned1')
farms = weeb.find_element(By.CSS_SELECTOR, 'div#product2')
farms_owned = weeb.find_element(By.CSS_SELECTOR, 'div#productOwned2')

# click cookie
while cursors_owned.text != '30':
    # click for 1 second
    for i in range(10):
        cookie.click()
        time.sleep(0.01)

    # check if there's upgrades
    try:
        upgrade = weeb.find_element(By.CSS_SELECTOR, 'div#upgrade0')
        if upgrade.get_attribute('class').__contains__('enabled'):
            upgrade.click()
    except: pass

    if farms.get_attribute('class').__contains__('enabled'):
        farms.click()
    if grandmas.get_attribute('class').__contains__('enabled'):
        grandmas.click()
    if cursors.get_attribute('class').__contains__('enabled'):
        cursors.click()

    # log stats
    print(cursors_owned.text)
else:
    print('Met the goal, closing in 60 seconds...')
    time.sleep(60)
    weeb.quit()
