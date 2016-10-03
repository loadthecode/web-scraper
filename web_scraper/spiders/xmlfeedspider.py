from scrapy import log
from scrapy.contrib.spiders import XMLFeedSpider
from web_scraper.items import TestItem
from scrapy import Item


class XmlfeedspiderSpider(XMLFeedSpider):
    name = "xmlfeedspider"
    start_urls = (
        'http://www.google.com/',
    )
    iterator = 'iternodes'
    itertags = 'item'    

    def parse(self, response, node):
	log.msg('%s %s ' % (self.itertag, ''.join(node.extract())))

	item = Item()
	item['id'] = node.select('@id').extract()
	item['name'] = node.select('name').extract()
	item['description'] = node.select('description').extract()
	return item        
