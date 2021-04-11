# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
import scrapy
import os

class PptPipeline:
    def process_item(self, item, spider):
        return item

class FileSave(FilesPipeline):
    def get_media_requests(self, item, info):
        if not os.path.exists('./ppts/' + item['dir_name'] + '/'):
            os.makedirs('./ppts/' + item['dir_name'] + '/')
        # print('准备下载文件：', item['down_href'])
        yield scrapy.Request(item['down_href'], meta={'dir_name': item['dir_name'], 'title':item['title']})

    def file_path(self, request, response=None, info=None, *, item=None):
        file_name = request.meta['dir_name'] + '/' + request.meta['title'] + '.zip'
        print('保存{}成功！'.format(request.meta['title']))
        return file_name
