from django.contrib import admin
from django.urls import path, include

from games.views import MainPage, StopGameNewsView, IgnNewsView, IgnHeadlineView, StopGameHeadlineView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view(), name="home"),
    path('stopgamenews/', StopGameNewsView.as_view()),
    path('accounts/', include('accounts.urls')),
    path('ignnews/<int:id>', IgnHeadlineView.as_view()),
    path('ignnews/', IgnNewsView.as_view()),
    path('stopgamenews/<int:id>', StopGameHeadlineView.as_view()),
]
