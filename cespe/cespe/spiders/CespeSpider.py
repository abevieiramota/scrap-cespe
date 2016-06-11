# -*- encoding: utf-8 -*-
import scrapy
from cespe.items import CespeItem

class CespeSpider(scrapy.Spider):
    
    name = "CespeSpider"
    start_urls = ("http://www.cespe.unb.br/concursos/",)
    
    def parse(self, response):
    
        for concurso_url_rel_path in response.xpath('//a[@class="Links"]/@href').extract():
        
            concurso_url = response.urljoin(concurso_url_rel_path)
            
            yield scrapy.Request(concurso_url, callback=self.parse_concurso)
    
    def parse_concurso(self, response):  
        
        files_urls_rel_path =  response.xpath('//a[contains(translate(@href, "PDF", "pdf"), ".pdf")]/@href').extract()
        files_urls = [response.urljoin(file_url_rel_path) for file_url_rel_path in files_urls_rel_path]
    
        item = CespeItem()
        item['file_urls'] = files_urls
        
        yield item
    
    