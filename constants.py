import requests
from bs4 import BeautifulSoup as bs
import random
import unidecode
API_KEY = '' #SET YOUR TELEGRAM TOKEN

BASE_URL = 'https://www.antoloji.com'
POETS_URL = BASE_URL + '/populer-sairler/sirala-/sayfa-'
POET_URL = BASE_URL + '/{}/'

def get_random_poet():
    poets = []
    for i in range(1, 16):
        req = requests.get(POETS_URL + str(i) + '/')
        soup = bs(req.content, 'html5lib')
        # print(soup.prettify())
        poet = soup.findAll('div', class_ = 'poem-title-pop')
        for i in poet:
            poets.append(i.a.text)
    s = unidecode.unidecode(random.choice(poets).lower()).replace(" ", "-").replace("(", "").replace(")","")
    return s

def get_random_poetry(poet):
    poetry_list = []
    for poetry in range(1,20):
        url = requests.get(POET_URL.format(poet) + '?sayfa=' + str(poetry))
        sp = bs(url.content, 'html5lib')
        poetries = sp.findAll('div', class_ = 'poem-title-pop')
        for p in poetries:
            poetry_list.append(p.find('a', href = True)['href'])

    ch_poetry = unidecode.unidecode(random.choice(poetry_list).lower()).replace(" ", "-")

    return BASE_URL + ch_poetry

def get_random_lines(poetry):
    poetry_lines = []
    req = requests.get(poetry)
    soup = bs(req.content, 'html5lib')
    pd_poem = soup.findAll('div', class_ = "pd-text")[0].findAll('p')
    for i in pd_poem:
        poetry_lines.append(i.text)
    ch_lines = random.choice(poetry_lines)
    return ch_lines
