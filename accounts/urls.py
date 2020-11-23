from django.urls import path

from .views import signup, logout_view, loginPage

urlpatterns = [
    path('login/', loginPage, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout'),
]
