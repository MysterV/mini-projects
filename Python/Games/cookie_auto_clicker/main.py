import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pyperclip import copy as copy_to_clipboard
import os
import shutil
import time

# A Cookie Clicker bot with built-in save system (progress is saved to 'save.txt')

# ===== Config =====
goal_productID = 9  # higher == better, counting up from 0 - cursor
goal_count = 10


# ===== Code =====
# Selenium setup
weeb = webdriver.Chrome()
weeb_conf = webdriver.ChromeOptions()
weeb_conf.add_experimental_option('detach', True)
weeb.get('https://orteil.dashnet.org/cookieclicker/')

# Select language and load up the UI
button_language_select = None
while not button_language_select:
    try:
        button_language_select = weeb.find_element(By.CSS_SELECTOR, 'div#langSelect-EN')
        break
    except: pass
button_language_select.click()
time.sleep(1)
# accept the cookies
button_accept_cookies = None
while not button_accept_cookies:
    try:
        button_accept_cookies = weeb.find_element(By.CSS_SELECTOR, f'a.cc_btn_accept_all')
        button_accept_cookies.click()
        break
    except: pass


# Find cookie and available products (aka buildings)
cookie = weeb.find_element(By.CSS_SELECTOR, 'button#bigCookie')
# add cursor to products list
products = {0: weeb.find_element(By.CSS_SELECTOR, f'div#product{0}')}
products_owned = {0: weeb.find_element(By.CSS_SELECTOR, f'div.title.owned#productOwned{0}')}
# try adding all available products to the list
highest_productID = 0
while True:
    try:
        highest_productID += 1
        products[highest_productID] = weeb.find_element(By.CSS_SELECTOR, f'div#product{highest_productID}')
        products_owned[highest_productID] = weeb.find_element(By.CSS_SELECTOR, f'div.title.owned#productOwned{highest_productID}')
    except selenium.common.exceptions.NoSuchElementException:
        break
    # products = {i: weeb.find_element(By.CSS_SELECTOR, f'div#product{i}') for i in range(highest_productID + 1)}
    # products_owned = {i: weeb.find_element(By.CSS_SELECTOR, f'div.title.owned#productOwned{i}') for i in range(highest_productID + 1)}


# Add saving functionality
button_options = weeb.find_element(By.XPATH, '//div[text() = "Options"]')
save = None
def export_save():
    global save
    button_options.click()
    try:
        button_export = weeb.find_element(By.XPATH, '//a[text() = "Export save"]')
        button_export.click()
    except selenium.common.exceptions.NoSuchElementException:
        button_options.click()
        button_export = weeb.find_element(By.XPATH, '//a[text() = "Export save"]')
        button_export.click()
    save = weeb.find_element(By.CSS_SELECTOR, 'textarea#textareaPrompt').text

    # backup
    with open('save.txt', 'wt') as f: f.close()
    os.makedirs('Backups', exist_ok=True)
    shutil.copy('save.txt', f'Backups/save_{time.strftime('%Y-%m-%d_%H%M', time.gmtime(time.time()))}.txt')
    # save
    with open('save.txt', 'wt') as f:
        f.write(save)
        print('Saved the game')
    # return to baking
    button_close_export = weeb.find_element(By.XPATH, '//a[text() = "All done!"]')
    button_close_export.click()
    button_options.click()


def import_save():
    global save
    try:
        with open('save.txt', 'rt') as f:
            save = f.read()
    except FileNotFoundError:
        print('No save game found')
        return
    button_options.click()
    try:
        button_import = weeb.find_element(By.XPATH, '//a[text() = "Import save"]')
        button_import.click()
    except selenium.common.exceptions.NoSuchElementException:
        button_options.click()
        button_import = weeb.find_element(By.XPATH, '//a[text() = "Import save"]')
        button_import.click()
    textbox = weeb.find_element(By.CSS_SELECTOR, 'textarea#textareaPrompt')
    # textbox.send_keys(save, Keys.RETURN)
    # asking Selenium to type out the savefile would freeze the browser for 5 seconds, so we use pyperclip instead
    copy_to_clipboard(save)
    textbox.send_keys(Keys.CONTROL + 'v', Keys.ENTER)
    button_options.click()


import_save()
time_loop_start = time.time()
while products_owned[goal_productID].text != str(goal_count):
    # autosave every 2 minutes
    if time.time() - time_loop_start >= 120:
        time.sleep(0.01)
        export_save()
        time.sleep(0.01)
        time_loop_start = time.time()
        # log stats
        if products_owned[goal_productID].text:
            print(
                f'goal: {products[goal_productID].text.split('\n')[0]}\t{products_owned[goal_productID].text}/{goal_count}')
        else:
            print(f'goal: {products[goal_productID].text.split('\n')[0]}\t0/{goal_count}')

    # click the cookie a bunch
    try:
        for i in range(20):
            cookie.click()
            time.sleep(0.01)  # 100cps
    except: pass

    # look for the golden cookie
    try:
        golden_cookies = weeb.find_elements(By.CSS_SELECTOR, 'div.shimmer')
        if golden_cookies:
            for i in golden_cookies:
                i.click()
    except: pass

    # check for upgrades (unlike products they disappear when bought)
    try:
        upgrade = weeb.find_element(By.CSS_SELECTOR, 'div#upgrade0')
        if upgrade.get_attribute('class').__contains__('enabled'):
            upgrade.click()
    except: pass

    # buy products
    for i in range(highest_productID-1, 0, -1):
        # are there better options?
        if products_owned[i].text:
            # is it time to buy the next thing?
            if int(products_owned[i].text) > 10 and not products_owned[i+1].text:
                break
            # are you neglecting the previous thing? (also the only way to buy cursors)
            if not products_owned[i-1].text or int(products_owned[i].text)+10 > int(products_owned[i-1].text):
                if products[i-1].get_attribute('class').__contains__('enabled'):
                    products[i-1].click()
        # if not, buy this
        if products[i].get_attribute('class').__contains__('enabled'):
            products[i].click()
            # if it's the last upgrade on shopping list, add the next product to the list
            if products_owned[i].text:
                if i == max(products.keys()):
                    highest_productID += 1
                    products[highest_productID] = weeb.find_element(By.CSS_SELECTOR, f'div#product{highest_productID}')
                    products_owned[highest_productID] = weeb.find_element(By.CSS_SELECTOR, f'div.title.owned#productOwned{highest_productID}')


    # TODO:
    # figure out how to balance upgrades vs products


print('Met the goal, closing in 10 seconds...')
export_save()
time.sleep(60)
weeb.quit()
