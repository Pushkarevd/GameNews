import requests
from bs4 import BeautifulSoup

URL = "https://stopgame.ru/news"


def stopgame_get_news():
    html = requests.get(URL).text
    soup = BeautifulSoup(html, "html.parser")

    headlines = []
    for number, news in enumerate(soup.find_all("div", {"class": "item article-summary"})):
        img_src = news.find("div", {"class": "image lazy"}).get("data-src")
        desc = news.find("div", {"class": "caption caption-bold"}).get_text()
        url = "https://stopgame.ru" + news.find("div", {"class": "caption caption-bold"}).a.get("href")
        headlines.append({"img": img_src, "desc": desc, "url": url})
        if number == 7:
            break
    return headlines


def get_img():
    html = requests.get(URL).text
    soup = BeautifulSoup(html, "html.parser")

    imgs = []
    for number, news in enumerate(soup.find_all("div", {"class": "item article-summary"})):
        img_src = news.find("div", {"class": "image lazy"}).get("data-src")
        imgs.append(img_src)
        if number == 5:
            break
    return imgs


def stopgame_headline(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("section", {"class": "article-header"})
    headline = soup.find("section", {"class": "article"})

    return (title, headline)
