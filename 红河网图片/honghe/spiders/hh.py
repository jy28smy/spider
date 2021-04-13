import scrapy
from pyquery import PyQuery as pq
import json
from ..items import HongheItem
import re
import requests

class HhSpider(scrapy.Spider):
    name = 'hh'

    def start_requests(self):
        url = 'http://tuku.hh.cn/list1/15-16'
        yield scrapy.Request(url, callback=self.get_id_one_class)

    def get_id_one_class(self, response):
        html = response.text
        url = 'http://tuku.hh.cn/respository'
        info_url = 'http://tuku.hh.cn/respository/info'
        dics = re.findall(r'"sub_respository":\[(.*?)\]};', html)
        dics_list = dics[0].replace('],"old_photo":[', ',').replace('},{', '}@{').split('@')
        for dic in dics_list:
            item = HongheItem()
            dic = json.loads(dic)
            i_d = dic['id']
            item['one_class'] = dic['name']
            count_data = {
                'i': str(i_d),
                't': '3',
                'callback': 'jQuery111204507538242328981_1618236090086',
            }
            hd = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
            h = requests.post(info_url, data=count_data, headers=hd).text
            d_count = json.loads(h.split('(')[1].split(')')[0])
            count = int(d_count['c_n'])
            for i in range(0, count + 20, 20):
                data = {
                    'id': str(i_d),
                    'start': str(i),
                    'cnt': '20',
                    'callback': 'jQuery111205435798931123299_1618229472875'
                }
                yield scrapy.FormRequest(url, formdata=data, meta={'item': item}, callback=self.parse, dont_filter=True)

    def parse(self, response, **kwargs):
        j = response.text
        d_str = json.loads(j.split('(', 1)[1].rsplit(')', 1)[0])
        for d in d_str['data']:
            item = response.meta['item']
            two_href = 'http://tuku.hh.cn/' + d['href']
            item['two_class'] = d['title']
            yield scrapy.Request(two_href, meta={'item': item}, callback=self.detail_parse)

    def detail_parse(self, response):
        html = response.text
        datas_list = re.findall(r'var data=\[(.*)\];', html)
        dict_list = datas_list[0].replace('},{', '}@{').split('@')
        for d in dict_list:
            d_data = json.loads(d)
            item = response.meta['item']
            item['img_name'] = d_data['description']
            item['img_url'] = 'http://tuku.hh.cn/' + d_data['file'].replace('\\', '')
            yield item