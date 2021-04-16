import scrapy
import json
from lxml import etree


class JdcySpider(scrapy.Spider):
    name = 'jdcy'
    # allowed_domains = ['www.mafengwo.cn']
    # start_urls = ['https://www.mafengwo.cn/ajax/router.php/']

    def start_requests(self):
        for i in range(1, 21):
            url = 'https://m.mafengwo.cn/jd/11871/gonglve.html?page={}&is_ajax=1'.format(i)
            yield scrapy.Request(url, callback=self.one_parse)

    def one_parse(self, response, **kwargsgs):
        comments_url = 'https://m.mafengwo.cn/poi/poi/comment_page'
        html = json.loads(response.text)['html']
        r = etree.HTML(html)
        lst = r.xpath('//a[@class="poi-li"]')
        for l in lst:
            item = {}
            href = ''.join(l.xpath('./@href'))
            id = href.split('.')[0].rsplit('/')[-1]
            item['name'] = l.xpath('./div[1]/text()')[0]
            page = 1
            data = {
                'poiid': id,
                'page': str(page)
            }
            yield scrapy.FormRequest(comments_url, formdata=data, meta={'id': id, 'item': item, 'page': page}, callback=self.two_parse, dont_filter=True)

    def two_parse(self, response):
        id = response.meta['id']
        item = response.meta['item']
        page = response.meta['page']
        r = json.loads(response.text)

        html = r['html']
        e = etree.HTML(html)
        item['comments'] = e.xpath('//div[@class="context line5"]/text()')
        comments_url = 'https://m.mafengwo.cn/poi/poi/comment_page'
        if r['moreComment']:
            page += 1
            data = {
                'poiid': id,
                'page': str(page)
            }
            yield scrapy.FormRequest(comments_url, formdata=data, meta={'id': id, 'item': item, 'page': page},
                                     callback=self.two_parse, dont_filter=True)
        yield item
