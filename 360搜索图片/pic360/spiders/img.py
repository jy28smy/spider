import scrapy
import json
from ..items import Pic360Item
import os

class ImgSpider(scrapy.Spider):
    name = 'img'
    allowed_domains = ['www.so.com', 'qhimgs1.com']
    if not os.path.exists('./360pic/copyright/'):
        os.makedirs('./360pic/copyright/')
    def start_requests(self):
        for i in range(1,1000):
            url = 'https://image.so.com/zjl?ch=copyright&sn={}'.format(i*30)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        re = json.loads(response.text)
        for con in re['list']:
            item = Pic360Item()
            item['img_url'] = con['qhimg_url']
            item['title'] = con['title']
            item['id'] = con['id']
            yield item
