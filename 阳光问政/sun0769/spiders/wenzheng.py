import scrapy


class WenzhengSpider(scrapy.Spider):
    name = 'wenzheng'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest']

    def parse(self, response):
        next_page_url = 'http://wz.sun0769.com'+response.xpath('//div[@class="mr-three paging-box"]/a[2]/@href').extract_first()
        if next_page_url != 'http://wz.sun0769.com/political/index/politicsNewest?id=1&page=101':
            yield scrapy.Request(next_page_url,callback=self.parse)
        hrefs = response.xpath('//ul[@class="title-state-ul"]/li')
        for url in hrefs:
            detail_url = 'http://wz.sun0769.com'+url.xpath('./span/a/@href').extract_first()
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail)

    def parse_detail(self,response):
        item = {}
        item['title'] = response.xpath('//div[@class="mr-three"]/p/text()').extract_first()
        item['code'] = response.xpath('//div[@class="focus-date clear focus-date-list"]/span[4]/text()').extract_first()
        item['content'] = response.xpath('//pre/text()').extract_first()
        item['date'] = response.xpath('//div[@class="focus-date clear focus-date-list"]/span[2]/text()').extract_first()
        yield item

