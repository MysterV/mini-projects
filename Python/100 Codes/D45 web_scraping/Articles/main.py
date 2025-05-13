from bs4 import BeautifulSoup
import requests as rq

site1 = open('website.html').read()
site1_soup = BeautifulSoup(site1, 'html.parser')

print(site1_soup.title.string)

for i in site1_soup.find_all('a'):
    print(i.get('href'))

# =====

response = rq.get('https://news.ycombinator.com/news')
response.raise_for_status()
site2 = response.text
site2_soup = BeautifulSoup(site2, 'html.parser')

# print(site2_soup.select_one('.titleline > a').get_text())
# print(site2_soup.select_one('.titleline > a').get('href'))
# print(site2_soup.select_one('span .score').get_text())

articles = site2_soup.select('.titleline > a')
articles_text = [art.get_text() for art in articles]
articles_links = [art.get('href') for art in articles]
articles_ratings = [int(score.get_text().split()[0]) for score in site2_soup.select('span .score')]

highest_rating_id = articles_ratings.index(max(articles_ratings))

print(articles_text[highest_rating_id])
print(articles_links[highest_rating_id])
print(articles_ratings[highest_rating_id])
