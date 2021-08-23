# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestScrapyItem(scrapy.Item):
    # define the fields for your item here like:
        # 职位
    position = scrapy.Field()  # 职位类型
    position_type = scrapy.Field()
    # 招聘人数
    persons = scrapy.Field()
    # 工作地点
    place = scrapy.Field()
    # 招聘发布时间
    time = scrapy.Field()
    # 职位详细链接
    detail_link = scrapy.Field()
    # 工作职责
    work_duty = scrapy.Field()
    # 工作要求
    work_request = scrapy.Field()
