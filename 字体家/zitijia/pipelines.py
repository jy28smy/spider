# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
import scrapy
import os
import requests
from fake_useragent import UserAgent


class FilesPl(FilesPipeline):

    def get_media_requests(self, item, info):
        dir_path = './字体/{}/{}/{}'.format(item['class_one'], item['class_two'], item['font_name'])
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        self.get_img(item, dir_path)
        yield scrapy.Request(item['file_url'], meta={'meta': item})

    def get_img(self, item, p):
        if item['font_img']:
            headers = {'User-Agent': UserAgent().random}
            for img in item['font_img']:
                r_img = requests.get(img, headers=headers).content
                img_end = img.split('?')[0].rsplit('/')[-1]
                img_path = p + '/' + img_end
                with open('./' + img_path, 'wb') as f:
                    f.write(r_img)
        else:
            print('好家伙，居然没有图片！然则，并没过滤letter.png是不应该没有图片的，只是以防万一！')
        return item

    def file_path(self, request, response=None, info=None, *, item=None):
        item = request.meta['meta']
        file_name = './{}/{}/{}'.format(item['class_one'], item['class_two'], item['font_name']) + '/' + item['font_name'] + '.zip'
        return file_name


    def item_completed(self, results, item, info):
        return item  # 返回给下一个即将被执行的管道类



class ZitijiaPipeline:
    def process_item(self, item, spider):
        return item
