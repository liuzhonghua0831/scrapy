# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field() # 日期
    week = scrapy.Field() # 星期
    weather = scrapy.Field() # 天气
    temperature = scrapy.Field() # 温度
    wind = scrapy.Field() # 风力