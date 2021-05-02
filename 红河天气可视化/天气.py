'''
=====================日期：2021年05月01日=====================
'''
from pyecharts.charts import Bar, Grid, Line, Map
import pyecharts.options as opts
from pyecharts.globals import ThemeType
import jieba
import pandas as pd
from pyecharts.charts import WordCloud


def get_year_mean(file):
    '''获取年平均气温,最高温，最低温'''
    df = pd.read_excel(file, engine='openpyxl')
    mean_value = []
    max_value = []
    min_value = []
    for i in range(11, 22):
        d = df.loc[df["日期"].str.startswith("20{}-".format(i)), :]
        mean_value.append('%.2f' % ((d['最高气温'].mean() + d['最低气温'].mean()) / 2))
        max_value.append(int(d['最高气温'].max()))
        min_value.append(int(d['最低气温'].min()))
    return mean_value, min_value, max_value


def get_good_day(file):
    '''获取温度适宜的天数'''
    df = pd.read_excel(file, engine='openpyxl')
    good_day = df.loc[(df["最高气温"] <= 24) & (df["最低气温"] >= 17), :]
    return len(good_day)


def get_count(file):
    '''将文本文件的词统计成元组形式的列表'''
    text = open(file, 'r', encoding='utf-8').read()
    jieba.setLogLevel(jieba.logging.INFO)
    words = jieba.lcut(text)
    dic = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            dic[word] = dic.get(word, 0) + 1

    list = []
    for k in dic:
        if dic[k] > 1:
            list.append((k, dic[k]))
    return list


# 文件路径
gj_file = './datas/个旧历史天气.xlsx'
ky_file = './datas/开远历史天气.xlsx'
mz_file = './datas/蒙自历史天气.xlsx'
js_file = './datas/建水历史天气.xlsx'

# 适宜天数
gj_good_day = get_good_day(gj_file)
ky_good_day = get_good_day(ky_file)
mz_good_day = get_good_day(mz_file)
js_good_day = get_good_day(js_file)

# 年平均气温
gj_mean, gj_min_value, gj_max_value = get_year_mean(gj_file)
ky_mean, ky_min_value, ky_max_value = get_year_mean(ky_file)
mz_mean, mz_min_value, mz_max_value = get_year_mean(mz_file)
js_mean, js_min_value, js_max_value = get_year_mean(js_file)

# 柱状图，适宜天数
bar = (
    Bar()
        .add_xaxis(['个旧', '开远', '蒙自', '建水'])
        .add_yaxis('天数', [gj_good_day, ky_good_day, mz_good_day, js_good_day], bar_width=50)
        .set_global_opts(
        title_opts=opts.TitleOpts(title='舒适温度天数', subtitle='17度 < 温度 < 24度', pos_top="6%", pos_left='5%', ),
        legend_opts=opts.LegendOpts(pos_left="20%", pos_top="8%"),
        graphic_opts=opts.GraphicText(graphic_item=opts.GraphicItem(left="center", top="2%", z=100),
                                      graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                                          text='2011年1月至2021年4月个旧、开远、蒙自、建水气温分析',
                                          font="28px Microsoft YaHei",
                                          graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(fill="#259FA1")
                                      )
                                      )
    )
        .set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最好"),
                opts.MarkPointItem(type_="min", name="最差"),
            ]
        )))
bar.reversal_axis()

# 折线图，年平均气温
line = (
    Line()
        .add_xaxis(['2011年', '2012年', '2013年', '2014年', '2015年', '2016年', '2017年', '2018年', '2019年', '2020年'])
        .add_yaxis("个旧", gj_mean, is_smooth=True)
        .add_yaxis("开远", ky_mean, is_smooth=True)
        .add_yaxis("蒙自", mz_mean, is_smooth=True)
        .add_yaxis("建水", js_mean, is_smooth=True)
        .set_global_opts(title_opts=opts.TitleOpts(title="年平均温度", pos_left='5%', pos_top='55%'),
                         legend_opts=opts.LegendOpts(pos_top="55%", pos_left='15%'),
                         yaxis_opts=opts.AxisOpts(min_=14, max_=24))
        .set_series_opts(linestyle_opts=opts.LineStyleOpts(width=5))
)

# 柱状图，最高最低气温
bar_lh = (
    Bar()
        .add_xaxis(['2011年', '2012年', '2013年', '2014年', '2015年', '2016年', '2017年', '2018年', '2019年', '2020年'])
        .add_yaxis('个旧最低温', gj_min_value, stack="stack1")
        .add_yaxis('个旧最高温', gj_max_value, stack="stack1")
        .add_yaxis('开远最低温', ky_min_value, stack="stack2")
        .add_yaxis('开远最高温', ky_max_value, stack="stack2")
        .add_yaxis('蒙自最低温', mz_min_value, stack="stack3")
        .add_yaxis('蒙自最高温', mz_max_value, stack="stack3")
        .add_yaxis('建水最低温', js_min_value, stack="stack4")
        .add_yaxis('建水最高温', js_max_value, stack="stack4")
        .set_global_opts(title_opts=opts.TitleOpts(title='年最高、最低温度', pos_left='66%', pos_top="7%"),
                         legend_opts=opts.LegendOpts(pos_left="75%", pos_top="5%"),
                         yaxis_opts=opts.AxisOpts(min_=-5, max_=45))
)

# 地图，人口密度
MAP_DATA = [
    ["个旧市", 330],
    ["开远市", 149],
    ["蒙自市", 72],
    ["建水县", 143],
    ["弥勒市", 125],
    ["屏边苗族自治县", 84],
    ["石屏县", 95],
    ["泸西县", 227],
    ["元阳县", 208],
    ["红河县", 134],
    ["金平苗族瑶族傣族自治县", 87],
    ["绿春县", 81],
    ["河口县", '没有数据']
]

m = (
    Map(init_opts=opts.InitOpts())
    .add(
        series_name="红河州各县市人口密度",
        maptype="红河哈尼族彝族自治州",
        data_pair=MAP_DATA,
        is_map_symbol_show=True,
        zoom=0.8
    )
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{b}<br/>{c} (人 / km2)"
        ),
        visualmap_opts=opts.VisualMapOpts(
            range_color=["lightskyblue", "yellow", "orangered"],
        ),
        legend_opts=opts.LegendOpts(pos_top="15%", item_height=24, item_width=30, textstyle_opts=opts.TextStyleOpts(font_size=18, color='#28b2c7'))
    )
)

# 词云 词条热词
words = get_count('honghe.txt')
yun = (
    WordCloud()
        .add("", words, word_size_range=[5, 40], shape='star', width=640, height=480, pos_top='50%', pos_right='5%', pos_left='66%')
        .set_global_opts(title_opts=opts.TitleOpts(title="红河热词"))
)


grid = Grid(init_opts=opts.InitOpts(width="1920px", height="960px", page_title='红河天气', theme=ThemeType.MACARONS))
grid.add(bar, grid_opts=opts.GridOpts(pos_top='9%', pos_bottom='54%', pos_left='5%', pos_right='66%'))
grid.add(bar_lh, grid_opts=opts.GridOpts(pos_top='9%', pos_bottom='54%', pos_right='5%', pos_left='66%'))
grid.add(line, grid_opts=opts.GridOpts(pos_top='60%', pos_right='66%', pos_left='5%'))
grid.add(yun, grid_opts=opts.GridOpts())
grid.add(m, grid_opts=opts.GridOpts())

grid.render('2011-2021红河州天气情况.html')
