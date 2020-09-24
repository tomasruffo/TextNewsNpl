# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:38:17 2020

@author: Tomas
"""

from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup



# Defino una abstraccion para cada tipo de informacion que quiero extraer
# Cada una tiene sus propias propiedades diferentes
# REVIEW



class Articulo(Item):
    titulo = Field()
    contenido = Field()
    fecha = Field()


class LaNacionCrawl(CrawlSpider):
    name = 'LaNacion'
    custom_settings = {
      'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
      'CLOSESPIDER_PAGECOUNT': 3 # Un poco alto
    }

    

    allowed_domains = ['lanacion.com.ar','buscar.lanacion.com.ar']
    start_urls = ['https://buscar.lanacion.com.ar/economia']
    download_delay = 1

    rules = (

       #Paginacion
        Rule(
            LinkExtractor(
            allow=r'page-'
            ), follow=True),

        #Detalle de los productos
        Rule(
        LinkExtractor(
        allow=r'-nid'
                ), follow = True, callback = parse_review),
        )

    def parse_review(self, response):
        item = ItemLoader(Articulo(), response)
        item.add_xpath('titulo', '//h1@[class="titulo"]/text()')
        item.add_xpath('fecha', '//section[@class="fecha"]/text()')
        item.add_xpath('texto', '//p/text()')
        print(response.text)
        yield item.load_item()

    # DEFINICION DE CADA FUNCION PARSEADORA DE CADA TIPO DE INFORMACION


