# -*- coding: utf-8 -*-
from scrapy import log
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request
from web_scraper.items import TestItem

class GoogleSpider(BaseSpider):
    name = "google"
    allowed_domains = ["google.com"]
    start_urls = (
        'http://www.google.com/',
    )

    def parse(self, response):
        self.log('Response received from %s' % response.url)
	hxs = HtmlXPathSelector(response)
	for h3 in hxs.select('//h3').extract():
		yield TestItem(name=h3)

	for url in hxs.select('//a/@href').extract():
		yield Request(url, callback=self.parse)

	
