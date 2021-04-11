import scrapy
from ..items import PptItem


class PptsSpider(scrapy.Spider):
    name = 'ppts'
    # allowed_domains = ['www.1ppt.com']
    start_urls = ['http://www.1ppt.com/xiazai/']

    def parse(self, response, **kwargs):
        res = response.xpath('//div[@class="col_nav clearfix"]/ul/li/a')
        for r in res:
            item = PptItem()
            one_href = 'http://www.1ppt.com' + r.xpath('./@href').get()
            item['dir_name'] = r.xpath('./text()').get()
            # print('开始访问one_href：',one_href)
            yield scrapy.Request(one_href, meta={'item': item, 'url': one_href}, callback=self.parse_first)

    def parse_first(self, response):
        item = response.meta['item']
        hrefs = response.xpath('//ul[@class="tplist"]/li/a/@href')
        for href in hrefs:
            detail_url = 'http://www.1ppt.com' + href.get()
            # print('开始访问detail_url：',detail_url)
            yield scrapy.Request(detail_url, meta={'item': item}, callback=self.parse_second)

        pages = response.xpath('//ul[@class="pages"]/li/a/@href')
        one_url = response.meta['url']
        for page in pages:
            next_page = one_url + page.get()
            # print('开始访问next_page：',next_page)
            yield scrapy.Request(next_page, meta={'item': item, 'url': one_url},callback=self.parse_first)

    def parse_second(self, response):
        item = response.meta['item']
        down_page = 'http://www.1ppt.com' + response.xpath('//ul[@class="downurllist"]/li/a/@href').get()
        item['title'] = response.xpath('//h1/text()').get()
        # print('开始访问down_page：', down_page)
        yield scrapy.Request(down_page, meta={'item': item}, callback=self.parse_third)

    def parse_third(self, response):
        item = response.meta['item']
        item['down_href'] = response.xpath('//li[@class="c1"]/a/@href').get()
        yield item
