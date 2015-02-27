# -*- coding: utf-8 -*-
import scrapy


class CargocollectiveSpider(scrapy.Spider):
    name = "cargocollective"
    allowed_domains = ["cargocollective.com"]
    start_urls = (
        'http://www.cargocollective.com/',
    )

    def parse(self, response):
        for sel in response.xpath('//div'):
        	img = sel.xpath('//img/@href()').extract()
        	print img
