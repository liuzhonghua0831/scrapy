# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import pymysql

# 保存txt文件
class WeatherPipeline(object):
	def process_item(self, item, spider):
		base_dir = os.getcwd() # 获取当前位置
		filename = base_dir + '\\file\\weather.txt' # 文件名

		with open(filename, 'a', encoding='utf-8') as f:
			f.write(item['date'] + '\n')
			f.write(item['week'] + '\n')
			f.write(item['weather'] + '\n')
			f.write(item['temperature'] + '\n')
			f.write(item['wind'] + '\n\n')

		return item

# 保存json文件
class WPjson(object):
	def process_item(self, item, spider):
		base_dir = os.getcwd()
		filename = base_dir + '\\file\\weather.json'

		with open(filename, 'a', encoding='utf-8') as f:
			line = json.dumps(dict(item), ensure_ascii=False) + '\n'
			f.write(line)

		return item

# 保存到数据库
class WPmysql(object):
	def process_item(self, item, spider):
		date = item['date']
		week = item['week']
		weather = item['weather']
		temp = item['temperature']
		wind = item['wind']

		# 连接数据库
		connection = pymysql.connect(
			host = 'localhost',
			user = 'root',
			password = '123456',
			db = 'scrapyDB',
			charset = 'utf8mb4',
			cursorclass = pymysql.cursors.DictCursor)
		try:
			with connection.cursor() as cursor:
				sql = '''INSERT INTO WEATHER(date,week,weather,temperature,wind)
				         VALUES (%s,%s,%s,%s,%s)'''
				cursor.execute(sql, (date,week,weather,temp,wind))
			connection.commit()
		finally:
			connection.close()

		return item