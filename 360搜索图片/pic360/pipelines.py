# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class Pic360Pipeline:
    def process_item(self, item, spider):
        return item


class ImgPip(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['img_url'], meta={'title': item['title'], 'id': item['id']})

    def file_path(self, request, response=None, info=None, *, item=None):
        file_name = request.meta['title'] + '_' + request.meta['id'] + '.' + request.url.split('.')[-1]
        return file_name

    def item_completed(self, results, item, info):
        return item