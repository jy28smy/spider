import scrapy
from guazi.items import GuaziItem

class GzSpider(scrapy.Spider):
    name = 'gz'
    allowed_domains = ['www.guazi.com']
    start_urls = ['https://www.guazi.com/gejiu/buy/']

    def start_requests(self):
        for i in range(1,51):
            url = 'https://www.guazi.com/gejiu/buy/o{}/#bread'.format(i)
            yield scrapy.Request(url,callback=self.parse)

    def parse(self, response,**kwargs):
        # 解析数据
        li_list = response.xpath('//ul[@class="carlist clearfix js-top"]/li')
        for li in li_list:
            item = GuaziItem()
            item['title'] = li.xpath('./a/h2/text()').get()
            item['link'] = 'https://www.guazi.com' + li.xpath('./a/@href').get()
            item['price'] = li.xpath('.//div[@class="t-price"]/p/text()').get() + '万元'
            yield scrapy.Request(item['link'],meta={'meta':item},callback=self.detail_parse)
        # # 解析next_url
        # next_url = 0
        # try:
        #     next_url = 'https://www.guazi.com' + response.xpath('//a[@class="next"]/@href').get()
        # except TypeError:
        #     print('抓取完毕！')
        # finally:
        #     if next_url:
        #         yield scrapy.Request(next_url,callback=self.parse)

    def detail_parse(self,response):
        item = response.meta['meta']
        item['time'] = response.xpath('//li[@class="one"]/span/img/@src').get()
        item['mileage'] = response.xpath('//li[@class="two"]/span/text()').get()
        item['displacement'] = response.xpath('//li[@class="three"]/span/text()').get()
        item['gearbox'] = response.xpath('//li[@class="last"]/span/text()').get()
        if item['time'] and item['mileage'] and item['displacement'] and item['gearbox']:
            yield item