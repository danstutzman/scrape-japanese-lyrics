# -*- coding: utf-8 -*-
import scrapy


class HomepageSpider(scrapy.Spider):
    name = "homepage"
    allowed_domains = ["j-lyric.net"]
    start_urls = (
        'http://www.j-lyric.net/',
    )

    def parse(self, response):
        pass
