# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import SitemapSpider


class SitemapspiderSpider(SitemapSpider):
    sitemap_urls = ['http://www.google.com']
    sitemap_rules = [
	('/shop/', 'parse_shop'),	
    ]

    other_urls = ['http://gmail.com']
    
    def start_requests(self):
	requests = list(super(SitemapspiderSpider, self).start_requests())
	requests += [Request(x, callback=self.parse_other) for x in self.other_urls]
	return requests

    def parse_shop(self, response):
        pass

    def parse_other(self, response):
	pass
