# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZitijiaItem(scrapy.Item):
    # define the fields for your item here like:
    class_one = scrapy.Field()
    class_two = scrapy.Field()
    font_name = scrapy.Field()
    font_img = scrapy.Field()
    file_url = scrapy.Field()
