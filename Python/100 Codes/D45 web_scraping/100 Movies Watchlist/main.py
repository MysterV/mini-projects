import requests as rq
from bs4 import BeautifulSoup

URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = rq.get(URL)
response.raise_for_status()
site = response.text

site_soup = BeautifulSoup(site, 'html.parser')
movies = [title.get_text() for title in site_soup.select('div.article-title-description > div > h3')]
movies.reverse()

try:
    open('movies.txt', 'xt')
except FileExistsError:
    with open('movies.txt', 'wt', encoding='utf-8') as f:
        f.write('\n'.join(movies))

