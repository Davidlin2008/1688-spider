# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field,Item


class ProductItem(Item):
    # define the fields for your item here like:
    title = Field()
    shop = Field()
    price = Field()
    img = Field()
    