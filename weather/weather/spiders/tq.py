# -*- coding: utf-8 -*-
'''
获取未来一周天气情况
使用scrapy + xpath
'''


import scrapy
from weather.items import WeatherItem

class TqSpider(scrapy.Spider):
    name = 'tq'
    allowed_domains = ['tianqi.com']
    # start_urls = ['http://tianqi.com/']
    start_urls = [] # 创建url列表
    cities = ['suzhou', 'tianjin', 'beijing'] # 要获取天气信息的城市
    for city in cities:
    	start_urls.append('http://www.tianqi.com/' + city + '/')

    def parse(self, response):
        items = [] # 存储所有天气信息
        sevenday = response.xpath('.//div[@class="day7"]') # 获取信息所在位置
        name = sevenday.xpath('../div[@class="top"]/h1/text()').extract()[0] # 得到城市名

        date = sevenday.xpath('./ul[1]/li/b/text()').extract() # 获取日期
        week = sevenday.xpath('./ul[1]/li/span/text()').extract() # 获取星期
        weather = sevenday.xpath('./ul[2]/li/text()').extract() # 获取天气
        temp_max = sevenday.xpath('./div[@class="zxt_shuju"]/ul/li/span/text()').extract() # 最高温度
        temp_min = sevenday.xpath('./div[@class="zxt_shuju"]/ul/li/b/text()').extract() # 最低温度
        wind = sevenday.xpath('./ul[3]/li/text()').extract() # 获取风力情况

        for i in range(len(date)):
        	item = WeatherItem()
        	item['date'] = name[:4] + date[i]
        	item['week'] = week[i]
        	item['weather'] = weather[i]
        	item['temperature'] = str(temp_max[i]) + '° - ' + str(temp_min[i]) + '°'
        	item['wind'] = wind[i]
        	items.append(item)

        return items