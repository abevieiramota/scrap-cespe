# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
from cespe import settings
import os

class READMEPipeline(object):

    def process_item(self, item, spider):
    
        FILES_STORE = spider.settings.get('FILES_STORE')
        for file in item['files']:
        
            filename = '{}.README'.format(file['path'])
            filepath = os.path.join(FILES_STORE, filename)
            
            with open(filepath, 'wb') as f:
                
                file_info = csv.DictWriter(f, file.keys())
                file_info.writeheader()
                file_info.writerow(file)
        
        return item
