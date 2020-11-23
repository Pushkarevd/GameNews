from django.db import IntegrityError
from django.http import Http404
from django.shortcuts import render
from django.views import View

from games.ignparse import ign_get_news, ign_headline_parse
from games.models import StopGameHeadline, IgnHeadline
from games.stopgameparser import stopgame_get_news, get_img, stopgame_headline


def make_update():
    news = stopgame_get_news()
    for headline in news:
        id = StopGameHeadline.objects.count()
        try:
            StopGameHeadline.objects.create(desc=headline["desc"], img_url=headline["img"], news_url=headline["url"],
                                            id=id)
        except:
            IntegrityError
    news = ign_get_news()
    for headline in news:
        id = IgnHeadline.objects.count()
        try:
            IgnHeadline.objects.create(title=headline["title"], img_url=headline["img"], news_url=headline["url"],
                                       desc=headline["desc"], id=id)
        except:
            IntegrityError


class MainPage(View):
    def get(self, request):
        make_update()
        imgs = StopGameHeadline.objects.values()[:5]
        return render(request, "index.html", {"imgs": imgs})


class StopGameNewsView(View):
    def get(self, request):
        news = StopGameHeadline.objects.values()[:8]
        return render(request, "news.html", {"news": news, "flag": "stopgamenews/"})


class IgnNewsView(View):
    def get(self, request):
        news = IgnHeadline.objects.values()[:8]
        return render(request, "news.html", {"news": news, "flag": "ignnews/"})


class IgnHeadlineView(View):
    def get(self, request, id):
        try:
            headline = IgnHeadline.objects.get(id=id)
        except IgnHeadline.DoesNotExist:
            raise Http404
        html = ign_headline_parse(headline.news_url).prettify()

        return render(request, "ignheadline.html", {"html": html})

class StopGameHeadlineView(View):
    def get(self, request, id):
        try:
            headline = StopGameHeadline.objects.get(id=id)
        except IgnHeadline.DoesNotExist:
            raise Http404
        html = stopgame_headline(headline.news_url)

        return render(request, "ignheadline.html", {"title": html[0].prettify(), "article": html[1].prettify()})