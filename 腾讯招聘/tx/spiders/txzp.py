import scrapy
from tx.items import TxItem
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class TxzpSpider(scrapy.Spider):
    name = 'txzp'
    allowed_domains = ['careers.tencent.com']
    base_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1617197903405&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=40001&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn'
    start_urls = [base_url]
    rules = [
        Rule(LinkExtractor(allow=r'pageIndex=\d+&pageSize=10&language=zh-cn&area=cn'),callback='self.parse',follow=False)
    ]

    def parse(self, response):
        datas = response.json()['Data']['Posts']
        for data in datas:
            item = TxItem()
            item['job'] = data['RecruitPostName'].rsplit('-')[1]
            item['date_time'] = data['LastUpdateTime']
            item['city'] = data['LocationName']
            item['BG_name'] = data['BGName']
            item['bility'] = data['Responsibility']
            yield item
        # self.page_index += 1
        # yield scrapy.Request(self.base_url.format(self.page_index),callback=self.parse)