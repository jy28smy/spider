# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GuaziItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
    # 上牌时间
    time = scrapy.Field()
    # 里程
    mileage = scrapy.Field()
    # 排量
    displacement = scrapy.Field()
    # 变速箱
    gearbox = scrapy.Field()