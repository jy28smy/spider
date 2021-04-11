# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class Sun0769Pipeline:
    def process_item(self, item, spider):
        print(item)
        json.dump(item,open('json.txt', 'a', encoding='utf-8'), ensure_ascii=False)
        # with open('wz.json','a',encoding='utf-8') as f:
        #     f.write(item)
        return item
