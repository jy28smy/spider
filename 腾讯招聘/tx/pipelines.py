# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class TxPipeline:
    # 重写 __init__ 魔法方法，保存文件
    def __init__(self):
        self.file = open('txzp.json','a',encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii=False) + '\n'
        self.file.write(line)
        return item
    # 关闭文件
    def spider_close(self,spider):
        self.file.close()