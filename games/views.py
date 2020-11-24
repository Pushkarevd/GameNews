from django.db import IntegrityError
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View

from games.ignparse import ign_get_news, ign_headline_parse
from games.models import StopGameHeadline, IgnHeadline, Comment_StopGame, Comment_IGN
from games.stopgameparser import stopgame_get_news, stopgame_headline


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
        imgs = StopGameHeadline.objects.order_by("-id").values()[:5]
        return render(request, "index.html", {"imgs": imgs})


class StopGameNewsView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("home")
        news = StopGameHeadline.objects.order_by("-id").values()[:8]
        return render(request, "news.html", {"news": news, "flag": "stopgamenews/"})


class IgnNewsView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("home")
        news = IgnHeadline.objects.order_by("-id").values()[:8:-1]
        return render(request, "news.html", {"news": news, "flag": "ignnews/"})


class MainPageNewsView(View):
    def get(self, request, id):
        try:
            headline = StopGameHeadline.objects.get(id=id)
        except IgnHeadline.DoesNotExist:
            raise Http404
        html = stopgame_headline(headline.news_url)

        return render(request, "ignheadline.html", {"title": html[0].prettify(), "article": html[1].prettify()})


class IgnHeadlineView(View):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return redirect("home")
        try:
            headline = IgnHeadline.objects.get(id=id)
        except IgnHeadline.DoesNotExist:
            raise Http404
        html = ign_headline_parse(headline.news_url).prettify()

        return render(request, "ignheadline.html", {"html": html,
                                                    "headline": IgnHeadline.objects.get(id=id)})

    def post(self, request, id):
        text = request.POST.get("text")
        id = id
        Comment_IGN.objects.create(text=text, author=request.user, headline=IgnHeadline.objects.get(id=id))
        return redirect(request.path)


class StopGameHeadlineView(View):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return redirect("home")
        try:
            headline = StopGameHeadline.objects.get(id=id)
        except IgnHeadline.DoesNotExist:
            raise Http404
        html = stopgame_headline(headline.news_url)

        return render(request, "stopgameheadline.html", {"title": html[0].prettify(), "article": html[1].prettify(),
                                                    "headline": StopGameHeadline.objects.get(id=id)})

    def post(self, request, id):
        text = request.POST.get("text")
        id = id
        Comment_StopGame.objects.create(text=text, author=request.user, headline=StopGameHeadline.objects.get(id=id))
        return redirect(request.path)

