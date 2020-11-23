import requests
from bs4 import BeautifulSoup

URL = "https://ru.ign.com/?setccpref=RU"


def ign_get_news():
    html = requests.get(URL).text
    soup = BeautifulSoup(html, "html.parser")

    headline = []
    for number, news in enumerate(soup.find_all("article", {"class": "article NEWS"})):
        img = news.find("div", {"class": "t"}).img.get('src')
        tmp = news.find("div", {"class": "m"})
        title = tmp.h3.get_text()
        desc = tmp.p.get_text()
        url = tmp.a.get("href")
        headline.append({"img": img, "title": title, "desc": desc, "url": url})
        if number == 7:
            break

    return headline


def ign_headline_parse(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    return soup.find("article", {"class": "article-section article-page"})
