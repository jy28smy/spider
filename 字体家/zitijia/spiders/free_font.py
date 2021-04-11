import scrapy
from ..items import ZitijiaItem
import json
from urllib.parse import unquote

class FreeFontSpider(scrapy.Spider):
    name = 'free_font'
    def start_requests(self):
        for i in range(3, 4):
            item = ZitijiaItem()
            url = 'https://www.zitijia.com/cate/{}/'.format(i)
            if i == 1:
                item['class_one'] = '中文字体'
                yield scrapy.Request(url, meta={'meta1': item}, callback=self.cn_class_url_parse)
            elif i == 2:
                item['class_one'] = '英文字体'
                yield scrapy.Request(url, meta={'meta1': item}, callback=self.en_class_url_parse)
            elif i == 3:
                item['class_one'] = '图形字体'
                yield scrapy.Request(url, meta={'meta1': item}, callback=self.en_class_url_parse)

    def cn_class_url_parse(self, response):
        urls = response.xpath('//div[@class="item-nav el-card is-always-shadow"]/dl[3]/dd/a')
        for url in urls:
            item = response.meta['meta1']
            class_url = 'https://www.zitijia.com' + url.xpath('./@href').get() + '/'
            yield scrapy.Request(class_url, meta={'meta2': item}, callback=self.all_detail_page)

    def en_class_url_parse(self, response):
        item = response.meta['meta1']
        urls = response.xpath('//dl[1]/dd/a')
        for url in urls:
            class_url = 'https://www.zitijia.com' + url.xpath('./@href').get() + '/'
            yield scrapy.Request(class_url, meta={'meta2': item}, callback=self.all_detail_page)

    def all_detail_page(self, response):
        item = response.meta['meta2']
        item['class_two'] = unquote(response.url.rsplit('/')[-1]).split('?')[0]
        next_url = response.xpath('//a[@rel="next"]/@href').get()
        if isinstance(next_url, str):
            next_page = 'https://www.zitijia.com' + next_url
            yield scrapy.Request(next_page, meta={'meta2': item}, callback=self.all_detail_page)
        urls = response.xpath('//div[@class="item-list el-row"]/div')
        for url in urls:
            detail_page = 'https://www.zitijia.com' + url.xpath('.//a/@href').get()
            yield scrapy.Request(detail_page, meta={'meta3': item}, callback=self.detail_parse)

    def detail_parse(self, response):
        item = response.meta['meta3']
        r = response.xpath('//div[@class="item-info-price"]/text()')
        if r:
            price = r[1].get().strip()
            if price == '0.00 元':
                font_id = response.url.rsplit('/')[-1].split('.')[0]
                item['font_name'] = response.xpath('//div[@class="item-info-name"]/text()').get()
                imgs = response.xpath('//div[@id="item-shi"]//img/@src')
                item['font_img'] = ['https:' + img.get() for img in imgs]
                base_url = 'https://www.zitijia.com/downloadCheck'
                yield scrapy.FormRequest(base_url, formdata={'itemId': font_id}, meta={'meta4': item}, callback=self.parse, dont_filter=True)

    def parse(self, response, **kwargs):
        item = response.meta['meta4']
        r = response.text
        item['file_url'] = 'http:' + json.loads(r)['url']
        print('正在下载的文件：', item)
        yield item
