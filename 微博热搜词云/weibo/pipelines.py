# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from wordcloud import WordCloud
import jieba
# import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import time

class WeiboPipeline:
    def process_item(self, item, spider):
        t = item['words']
        w = ' '.join(jieba.lcut(t))
        font = '/font/msyhbd.ttc'
        bg_pic = np.array(Image.open("./weibo/font/aa.jpg"))
        # plt.figure()
        wc = WordCloud(max_font_size=60, scale=10.0, font_path=font, mask=bg_pic).generate(w)
        # plt.axis('off')
        # plt.imshow(wc)
        # plt.show()
        name = int(time.time())
        wc.to_file('./weibo/images/{}.png'.format(name))
        return item
