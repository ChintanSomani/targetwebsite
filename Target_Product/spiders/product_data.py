import re

import scrapy
from scrapy.cmdline import execute

class ProductDataSpider(scrapy.Spider):
    name = "target"

    def __init__(self, *args, **kwargs):
        super(ProductDataSpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('url')]

    def parse(self, response):
        txt = response.text.split("__TGT_DATA__': { configurable: false, enumerable: true, value: deepFreeze(JSON.parse(")[1].split('")),')[0].replace('\\','')
        item = {}
        try:
            item['url'] = response.xpath('//link[@rel="canonical"]/@href').get()
        except:
            item['url'] = ''
        try:
            item['tcin'] = ''.join(response.xpath('//div/b[contains(text(),"TCIN")]/following-sibling::text()').getall()).replace(': ', '')
        except:
            item['tcin'] = ''
        try:
            item['upc'] = ''.join(response.xpath('//div/b[contains(text(),"UPC")]/following-sibling::text()').getall()).replace(': ', '')
        except:
            item['upc'] = ''
        try:
            item['price_amount'] = re.findall('current_retail":(.*?),"external_system_id', txt)[0]
        except:
            item['price_amount'] = ''
        try:
            item['currency'] = '$'
        except:
            item['currency'] = ''
        try:
            item['description'] = re.findall('seo_description":"(.*?)","page_id', txt)[0]
        except:
            item['description'] = ''
        item['specs'] = None
        item['ingredients'] = []
        try:
            item['bullets'] = re.findall('"bullets":\["(.*?)"],"title', txt)[0]
        except:
            item['bullets'] = ''

        features_list = []
        try:
            key = 'Tire Type'
            value = response.xpath('//div/b[contains(text(),"Tire Type")]/following-sibling::text()').get().strip()
        except:
            value = ''
        features_list.append(key + ': ' + value)
        try:
            key = 'Material'
            value = response.xpath('//div/b[contains(text(),"Material")]/following-sibling::text()').get().strip()
        except:
            value = ''
        features_list.append(key + ': ' + value)
        try:
            key = 'Includes'
            value = response.xpath('//div/b[contains(text(),"Includes")]/following-sibling::text()').get().strip()
        except:
            value = ''
        features_list.append(key + ': ' + value)
        try:
            key = 'Care & Cleaning'
            value = response.xpath(
                '//div/b[contains(text(),"Care & Cleaning")]/following-sibling::text()').get().strip()
        except:
            value = ''
        features_list.append(key + ': ' + value)
        try:
            key = 'Suggested Age'
            value = response.xpath('//div/b[contains(text(),"Suggested Age")]/following-sibling::text()').get().strip()
        except:
            value = ''
        features_list.append(key + ': ' + value)
        try:
            key = 'Rear Wheel Diameter'
            value = response.xpath(
                '//div/b[contains(text(),"Rear Wheel Diameter")]/following-sibling::text()').get().strip()
        except:
            value = ''
        features_list.append(key + ': ' + value)
        try:
            key = 'Warranty'
            value = response.xpath('//div/b[contains(text(),"Warranty")]/following-sibling::text()').get().strip()
        except:
            value = ''
        features_list.append(key + ': ' + value)
        try:
            key = 'Min. Carseat Weight Supported'
            value = response.xpath(
                '//div/b[contains(text(),"Min. Carseat Weight Supported")]/following-sibling::text()').get().strip()
            # features_list.append(key + ': ' + value)
        except:
            value = ''
        features_list.append(key + ': ' + value)
        try:
            key = 'Battery'
            value = response.xpath('//div/b[contains(text(),"Battery")]/following-sibling::text()').get().strip()
        except:
            value = ''
        features_list.append(key + ': ' + value)
        try:
            key = 'Front Wheel Diameter'
            value = response.xpath(
                '//div/b[contains(text(),"Front Wheel Diameter")]/following-sibling::text()').get().strip()
        except:
            value = ''
        features_list.append(key + ': ' + value)
        try:
            key = 'Features'
            value = response.xpath('//div/b[contains(text(),"Features")]/following-sibling::text()').get().strip()
        except:
            value = ''
        features_list.append(key + ': ' + value)
        try:
            key = 'Product Configuration'
            value = response.xpath(
                '//div/b[contains(text(),"Product Configuration")]/following-sibling::text()').get().strip()
        except:
            value = ''
        features_list.append(key + ': ' + value)
        try:
            key = 'Max. Carseat Weight Capacity'
            value = response.xpath(
                '//div/b[contains(text(),"Max. Carseat Weight Capacity")]/following-sibling::text()').get().strip()
        except:
            value = ''
        features_list.append(key + ': ' + value)
        try:
            key = 'Max. Stroller Weight Capacity'
            value = response.xpath(
                '//div/b[contains(text(),"Max. Stroller Weight Capacity")]/following-sibling::text()').get().strip()
        except:
            value = ''
        features_list.append(key + ': ' + value)
        try:
            key = 'Dimensions (Collapsed)'
            value = response.xpath(
                '//div/b[contains(text(),"Dimensions (Collapsed)")]/following-sibling::text()').get().strip()
        except:
            value = ''
        features_list.append(key + ': ' + value)
        try:
            key = 'Assembly Details'
            value = response.xpath(
                '//div/b[contains(text(),"Assembly Details")]/following-sibling::text()').get().strip()
        except:
            value = ''
        features_list.append(key + ': ' + value)
        try:
            key = 'Industry or Government Certifications'
            value = response.xpath(
                '//div/b[contains(text(),"Industry or Government Certifications")]/following-sibling::text()').get().strip()
        except:
            value = ''
        features_list.append(key + ': ' + value)
        try:
            key = 'Weight'
            value = response.xpath('//div/b[contains(text(),"Weight")]/following-sibling::text()').get().strip()
        except:
            value = ''
        features_list.append(key + ': ' + value)
        try:
            key = 'Dimensions (Overall)'
            value = response.xpath(
                '//div/b[contains(text(),"Dimensions (Overall)")]/following-sibling::text()').get().strip()
        except:
            value = ''
        features_list.append(key + ': ' + value)
        item['features'] = features_list

        item['features'] = features_list

        yield item

