# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HongheItem(scrapy.Item):
    # define the fields for your item here like:
    one_class = scrapy.Field()
    two_class = scrapy.Field()
    img_name = scrapy.Field()
    img_url = scrapy.Field()
    pass
