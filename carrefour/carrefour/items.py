# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarrefourItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_id = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    brand = scrapy.Field()
    price = scrapy.Field()
    special_price = scrapy.Field()
    specification = scrapy.Field()
    strcategory = scrapy.Field()
