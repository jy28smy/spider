# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DaomuPipeline:
    def process_item(self, item, spider):
        file_name = item['name'] + '.txt'
        with open(item['path'] + file_name, 'w', encoding='utf-8') as f:
            f.write(item['content'])
        print(file_name + ' --> 保存到 /{} --> 成功!'.format(item['path']))
        return item
