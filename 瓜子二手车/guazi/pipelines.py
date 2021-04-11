# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class GuaziPipeline:
    def open_spider(self, spider):
        print('开始爬取……')
        self.fp = open('car.csv', 'a', encoding='GBK')
        self.fp.write('标题,价格,上牌时间,里程,排量,变速箱,详情链接\n')

    def process_item(self, item, spider):
        title = item['title'] + ','
        price = item['price'] + ','
        link = item['link'] + ','
        time = item['time'] + ','
        mileage = item['mileage'] + ','
        displacement = item['displacement'] + ','
        gearbox = item['gearbox'] + ','
        data = title + price + time + mileage + displacement + gearbox + link + '\n'
        self.fp.write(data)
        return item

    def close_spider(self, spider):
        print('爬取结束！')
        self.fp.close()
