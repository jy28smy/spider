import scrapy
from ..items import WeiboItem
import time


class RsSpider(scrapy.Spider):
    name = 'rs'
    allowed_domains = ['www.weibo.com']
    start_urls = ['https://s.weibo.com/top/summary']

    def parse(self, response, **kwargs):
        while True:
            strs = response.xpath('//tbody/tr//a/text()')
            t = ''
            for s in strs:
                t += s.get() + '\n'
            item = WeiboItem()
            item['words'] = t
            yield item
            time.sleep(180)
