# -*- coding: utf-8 -*-
from scrapy import log
from scrapy.contrib.spiders import CSVFeedSpider
from web_scraper.items import TestItem


class CsvfeedspiderSpider(CSVFeedSpider):
    name = "csvfeedspider"
    allowed_domains = ["google.com"]
    start_urls = (
        'http://www.google.com/',
    )
    delimiter = ':'
    headers = ['id', 'name', 'description']

    def parse_row(self, response, row):
        log.msg('Row %r' % row)

	item = TestItem()
	item['id'] = row['id']
	item['name'] = row['name']
	item['description'] = row['description']
	return item
