# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import matplotlib


class HhjdPipeline:
    def open_spider(self, spider):
        if not os.path.exists('./评论/'):
            os.mkdir('./评论/')

    def process_item(self, item, spider):
        with open('./评论/{}.txt'.format(item['name']), 'w', encoding='utf-8') as f:
            for comment in item['comments']:
                f.write(comment.strip())
        return item

    def close_spider(self, spider):
        ds = os.scandir(r'./评论')
        for d in ds:
            with open(d.path, 'r', encoding='utf-8') as f:
                comment = f.read()
                words = ''.join(jieba.lcut(comment))
                name = d.name.split('.')[0]
                print(words)
                plt.figure()
                matplotlib.rc("font", family='SimHei')
                bg_pic = np.array(Image.open(r'./hhjd/hh.png'))
                w = WordCloud(max_font_size=40,
                              font_path=r'C:\Windows\Fonts\msyh.ttc',
                              scale=5.0,
                              mask=bg_pic,background_color='white')
                plt.axis('off')
                plt.title(name + ' ===> 网友印象')
                wc = w.generate(words)
                plt.imshow(wc)
                # figManager控制全屏显示预览图片
                figManager = plt.get_current_fig_manager()
                figManager.full_screen_toggle()
                plt.show()
                w.to_file("./评论/{}.png".format(name))
