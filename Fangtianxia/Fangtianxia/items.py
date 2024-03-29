# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FangtianxiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    location = scrapy.Field()
    price = scrapy.Field()
    label = scrapy.Field()
    num = scrapy.Field()
    phone = scrapy.Field()
    neighbourhood = scrapy.Field()
    school_info = scrapy.Field()
