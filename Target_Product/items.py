# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class TargetProductItem(scrapy.Item):
    # Define the fields for your item here like:
    url = scrapy.Field()
    tcin = scrapy.Field()
    upc = scrapy.Field()
    price_amount = scrapy.Field()
    currency = scrapy.Field()
    description = scrapy.Field()
    bullets = scrapy.Field()
    features = scrapy.Field()
