from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pprint import pprint

weeb = webdriver.Edge()
weeb_conf = webdriver.EdgeOptions()
weeb_conf.add_experimental_option('detach', True)


def homework1():
    weeb.get('https://python.org/')
    event_times = weeb.find_elements(By.CSS_SELECTOR, 'div.event-widget > div > ul > li > time')
    event_names = weeb.find_elements(By.CSS_SELECTOR, 'div.event-widget > div > ul > li > a')
    events = {i: {'time': event_times[i].text, 'name': event_names[i].text} for i in range(len(event_names))}
    pprint(events)


def homework2():
    weeb.get('https://en.wikipedia.org/wiki/Main_Page')
    article_count = weeb.find_element(By.CSS_SELECTOR, '#articlecount > ul > li:nth-child(2) > a:nth-child(1)')
    print(article_count.text)


def homework3():
    pass
    # TODO: go to https://secure-retreat-92358.herokuapp.com/ and sign up for some sketchy newsletter


# homework1()  # done
# homework2()  # done
homework3()

weeb.quit()
