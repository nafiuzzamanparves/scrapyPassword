from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from scrapy.crawler import CrawlerProcess

from scrapers.spiders.hacker_news_spider import HackerNewsSpider
from scrapers.spiders.quotes_spider import QuotesSpider


def scrape_hacker_news(request):
    process = CrawlerProcess(
        settings={
            "FEEDS": {
                "items.json": {"format": "json"},
            },
        }
    )
    process.crawl(HackerNewsSpider)
    process.start()
    with open("items.json", "r") as f:
        data = f.read()

    return JsonResponse(data, safe=False)


def scrape_quotes(request):
    process = CrawlerProcess()
    process.crawl(QuotesSpider)
    process.start()

    return HttpResponse("Scraped quotes")
