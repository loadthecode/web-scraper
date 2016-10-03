# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item


class AmazonSpider(CrawlSpider):
    name = "amazon"
    allowed_domains = ["amazon.com"]
    start_urls = (
        'http://www.amazon.com/',
    )

    rules = (
	Rule(SgmlLinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),
        Rule(SgmlLinkExtractor(allow=('item\.php', )), callback='parse_item'),
    )

    def parse_item(self, response):
        self.log("Item page %s" % response.url)

	item = Item()

	item['id'] = hxs.select('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
	item['name'] = hxs.select('//td[@id="item_name"]/text()').extract()
	item['description'] = hxs.select('//td[@id="item_description"]/text()').extract()
	return item


