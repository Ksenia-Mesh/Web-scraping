import requests
import bs4
from bs4 import BeautifulSoup

HEADERS ={
    'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, lie Gecko) Chrome/96.0.4664.93 Safari/537.36'
}

KEYWORDS = ['Математика', 'IT', 'курса', 'python', 'Разработка', 'компьютеры', 'Блог', 'Карьера в IT-индустрии', 'JavaScript *']

buse_url = 'https://habr.com/ru/all/'

response = requests.get(buse_url, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')


for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = set(hub.text.strip() for hub in hubs)
    # print(hubs)

    for hub in hubs:
        if hub in KEYWORDS:
            href = article.find(class_='tm-article-snippet__title-link').attrs['href']
            link = 'https://habr.com' + href
            title = article.find('h2').find('span').text
            date = article.find_all(class_='tm-article-snippet__datetime-published')
            date = set(title.text.strip() for title in date)
            result = f'{date} - {title} - {link}'
            print(result)