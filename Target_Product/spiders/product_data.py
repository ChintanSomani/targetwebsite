import re
import scrapy
from scrapy.cmdline import execute

class ProductDataSpider(scrapy.Spider):
    name = "target"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('url')]

    def parse(self, response, **kwargs):
        txt = response.xpath('//script[contains(text(), "__TGT_DATA__")]/text()').re_first(r'__TGT_DATA__\': (.*?),\n', default='').replace('\\','')

        item = {
            'url': response.css('link[rel="canonical"]::attr(href)').get(default='').strip(),
            'tcin': self.extract_text(response, 'TCIN'),
            'upc': self.extract_text(response, 'UPC'),
            'price_amount': re.search(r'current_retail":(.*?),"external_system_id', txt).group(1),
            'currency': '$',
            'description': re.search(r'seo_description":"(.*?)","page_id', txt).group(1),
            'bullets': re.search(r'"bullets":\["(.*?)"],"title', txt).group(1),
            'specs': None,
            'ingredients': [],
            'features': self.extract_features(response)
        }

        yield item

    def extract_text(self, response, label):
        for i in range(1, 4):
            text = response.xpath(f'//*[@data-test="item-details-specifications"]/div//b[contains(text(),"{label}")]/following::text()[{i}]').get().replace(':', '').strip()
            if text:
                return text

    def extract_features(self, response):
        features_list = []
        features = response.css('[data-test="item-details-specifications"] div')
        for feature in features:
            key = feature.xpath('.//b//text()').get('').replace(':', '')
            value = self.extract_text(feature, key)
            if key and value:
                if f'{key}: {value}' not in features_list:
                    features_list.append(f'{key}: {value}')

        return features_list

