from django.urls import path
from .views import scrape_hacker_news, scrape_quotes

urlpatterns = [
    path("scrape-hacker-news/", scrape_hacker_news, name="scrape_hacker_news"),
    path("scrape-quotes/", scrape_quotes, name="scrape-quotes"),
]
