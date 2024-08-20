from django.shortcuts import render
from django.http import JsonResponse
from scrapy.crawler import CrawlerProcess
from scrapers.spiders.hacker_news_spider import HackerNewsSpider


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
