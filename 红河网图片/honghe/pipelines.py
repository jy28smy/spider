# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import os
import random

class HhImg(ImagesPipeline):

    def get_media_requests(self, item, info):
        path = '/{}/{}/'.format(item['one_class'], item['two_class'])
        if not os.path.exists('./hongheimg'+path):
            os.makedirs('./hongheimg'+path)
        yield scrapy.Request(item['img_url'], meta={'path': path})

    def file_path(self, request, response=None, info=None, *, item=None):
        path = request.meta['path']
        # 这里name有极低概率重名，如果要确保不重名可以和时间戳随便运算一下，或者直接用时间戳命名。
        name = random.randint(1000000, 999999999)
        img_name = path + str(name) + '.jpg'
        print('随便显示点什么，免得太尴尬！', img_name)
        return img_name

    def item_completed(self, results, item, info):
        return item





class HonghePipeline:

    def process_item(self, item, spider):
        return item
