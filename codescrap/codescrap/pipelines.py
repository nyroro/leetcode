# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class CodescrapPipeline(object):
    def open_spider(self, spider):
        if not os.path.exists('ac_code'):
            os.mkdir('ac_code')

    def process_item(self, item, spider):
        if item['lang'] == 'python':
            item['lang'] = 'py'
        filename = 'LC%s.%s'%(item['id'], item['lang'])
        with open('ac_code/%s'%filename, 'w') as f:
            f.write(item['code'])
        return item
