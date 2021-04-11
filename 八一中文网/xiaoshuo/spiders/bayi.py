import scrapy
import mongodb

# class BayiSpider(scrapy.Spider):
#     name = 'bayi'
#     allowed_domains = ['https://www.81zw.com/book/8816/874214.html']
#     start_urls = ['https://www.81zw.com/book/8816/874214.html']
#
#     def parse(self, response):
#         title = response.xpath('//h1/text()').extract_first()
#         content = ''.join(response.xpath('//div[@id="content"]/text()').extract()).replace('    ','\n')
#         # 推送数据到pipelines
#         yield {
#             'title':title,
#             'content':content
#         }
#         next_url = response.xpath('//div[@class="bottem1"]/a[3]/@href').extract_first()
#         # base_url = 'http://https://www.81zw.com{}'.format(next_url)
#         print(response.urljoin(next_url))
#         yield scrapy.Request(response.urljoin(next_url),callback=self.parse)