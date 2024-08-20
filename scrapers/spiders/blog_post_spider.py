import scrapy
from scrapers.models import BlogPost

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://myblog.com']

    def parse(self, response):
        for post in response.css('div.post'):
            title = post.css('h2 a::text').get()
            content = post.css('div.content::text').get()
            date_published = post.css('div.date::text').get()

            BlogPost.objects.create(
                title=title,
                content=content,
                date_published=date_published,
            )