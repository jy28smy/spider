import scrapy
import os

class DmbjSpider(scrapy.Spider):
    name = 'dmbj'
    allowed_domains = ['www.daomubiji.com']

    def start_requests(self):
        start_url = ''
        for i in range(1, 12):
            if i < 9:
                start_url = 'http://www.daomubiji.com/dao-mu-bi-ji-{}'.format(i)
            elif i == 9:
                start_url = 'http://www.daomubiji.com/dao-mu-bi-ji-2015'
            elif i == 10:
                start_url = 'http://www.daomubiji.com/sha-hai'
            elif i == 11:
                start_url = 'http://www.daomubiji.com/zang-hai-hua'
            yield scrapy.Request(start_url, callback=self.list_parse)

    def list_parse(self, response):
        list_urls = response.xpath('//article[@class="excerpt excerpt-c3"]/a/@href')
        for url in list_urls:
            item = {}       # item要在循环内定义，否则会被覆盖为最后一个url
            detail_url = url.get()
            item['url'] = detail_url
            if 'qi-xing-lu-wang' in item['url']:
                item['path'] = '盗墓笔记/七星鲁王/'
            elif 'nu-hai-qian-sha' in item['url']:
                item['path'] = '盗墓笔记/怒海潜沙/'
            elif 'qin-ling-shen-shu' in item['url']:
                item['path'] = '盗墓笔记/秦岭神树/'
            elif 'yun-ding-tian-gong' in item['url']:
                item['path'] = '盗墓笔记/云顶天宫/'
            elif 'she-zhao-gui-cheng' in item['url']:
                item['path'] = '盗墓笔记/蛇沼鬼城/'
            elif 'mi-hai-gui-chao' in item['url']:
                item['path'] = '盗墓笔记/谜海归巢/'
            elif '2-yin-zi' in item['url']:
                item['path'] = '盗墓笔记/第二季/引子/'
            elif 'yin-shan-gu-lou' in item['url']:
                item['path'] = '盗墓笔记/第二季/阴山古楼/'
            elif 'qiong-long-shi-ying' in item['url']:
                item['path'] = '盗墓笔记/第二季/邛笼石影/'
            elif 'dao-mu-bi-ji-7' in item['url']:
                item['path'] = '盗墓笔记/第二季/盗墓笔记7/'
            elif 'dajieju' in item['url']:
                item['path'] = '盗墓笔记/第二季/大结局/'
            elif '2015' in item['url']:
                item['path'] = '盗墓笔记/2015年更新/'
            elif 'shahai' in item['url']:
                item['path'] = '盗墓笔记/沙海/'
            elif 'zang-hai-hua' in item['url']:
                item['path'] = '盗墓笔记/藏海花/'
            else:
                print('这个网页没找到路径：', item['url'])
            if not os.path.exists(item['path']):
                os.makedirs(item['path'])
            yield scrapy.Request(detail_url, meta={'item':item},callback=self.parse)

    def parse(self, response, **kwargs):
        item = response.meta['item']
        item['name'] = response.xpath('//h1/text()').get().replace('?', '')
        contents = response.xpath('//article//text()')
        content = ''
        for i in contents:
            content += i.get().strip().replace('\\u3000', '') + '\n'
        item['content'] = content
        yield item
