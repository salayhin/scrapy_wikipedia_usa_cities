# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WikipediaUsaCitiesItem(scrapy.Item):
    # define the fields for your item here like:
    city = scrapy.Field()
    state = scrapy.Field()
    state_short_name = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)
    #pass
