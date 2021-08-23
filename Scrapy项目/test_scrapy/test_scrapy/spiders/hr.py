# -*- coding: utf-8 -*-
import scrapy
import re
from items import TencentItem
class HrSpider(scrapy.Spider):
     name = 'hr'
     allowed_domains = ['tencent.com']
     offset = 0
     original_url = 'https://hr.tencent.com/position.php?keywords=&tid=0&start='
     # 设置动态起始url
     start_urls = ['https://hr.tencent.com/position.php?keywords=&tid=0&start=' + str(offset)]

     def parse(self, response):
         # 编写xpath规则提取需要的数据，进行数据清洗。
         trs = response.xpath("//table[@class='tablelist']//tr")[1:-1]
         for tr in trs:
             item = TencentItem()
             item["position"] = tr.xpath("./td[1]/a/text()").extract()
             item["position_type"] = tr.xpath("./td[2]/text()").extract()
             item["persons"] = tr.xpath("./td[3]/text()").extract()
             item["place"] = tr.xpath("./td[4]/text()").extract()
             item["time"] = tr.xpath("./td[5]/text()").extract()
             link_part = tr.xpath("./td[1]/a/@href").extract_first()
             # 分析网址结构，拼接正确的职位详细链接
             url_detail = item["detail_link"] = 'https://hr.tencent.com/' + link_part
             # 将找到的详细链接yield 到scrapy的调度器，调度器进行入队列，依次发送请求。
             yield scrapy.Request(url=url_detail,
                                       callback=self.parse_next_url,#编写处理链接的回调函数
                                       meta = {"item":item},
                                       )
         # 进行翻页操作
         if self.offset < 2870:
             self.offset += 10
             url_send = self.original_url + str(self.offset)
             yield scrapy.Request(
                 url=url_send,
                 callback=self.parse,
                                  )
     # 编写回调函数
     def parse_next_url(self,response):
         item = response.meta["item"]
         item["work_duty"] = response.xpath("//table[@class='tablelist textl']//tr[3]//ul//text()").extract()
         item["work_request"] = response.xpath("//table[@class='tablelist textl']//tr[4]//ul//text()").extract()
         item["work_duty"] = re.sub(r'(\xa0)','',str(item["work_duty"]))
         item["work_request"] = re.sub(r'(\xa0)','',str(item["work_request"]))
         yield item