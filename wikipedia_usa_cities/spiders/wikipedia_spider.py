# -*- coding: utf-8 -*-

import scrapy
import pdb
from scrapy import Selector
from wikipedia_usa_cities.items import WikipediaUsaCitiesItem


class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"
    allowed_domains = ["wikipedia.org"]
    start_urls = [
        'https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population',
    ]

    def parse(self, response):
        body = response.xpath("//div[contains(@id,'mw-content-text')]//table[contains(@class, 'wikitable sortable') and contains(@style, 'text-align:center')]")[0].extract()
        sel = Selector(text=body.encode('utf-8'), type="html")
        cities = sel.xpath('//table/tr').extract()

        for city in cities[1:]:
            tr = Selector(text=city.encode('utf-8'), type="html")
            co_ordinate = tr.xpath("//tr/td[9]/small/span[contains(@class, 'plainlinks nourlexpansion')]/a/span[3]/span[1]/span[2]/span/text()").extract_first()

            yield {
                'city': self._find_city(city.encode('utf-8'), tr),
                'state': tr.xpath("//tr/td[3]/a/text()").extract_first(),
                'state_short_name': self._find_state_short_name(tr.xpath("//tr/td[3]/a/text()").extract_first()),
                'latitude': co_ordinate.split(';')[0],
                'longitude': co_ordinate.split(';')[1]
            }

    def _find_city(self, content, tr):

        if self._is_valid_xpath(content, "//tr/td[2]/i/a"):
            return tr.xpath("//tr/td[2]/i/a/text()").extract_first()
        elif self._is_valid_xpath(content, "//tr/td[2]/i/b/a"):
            return tr.xpath("//tr/td[2]/i/b/a/text()").extract_first()
        elif self._is_valid_xpath(content, "//tr/td[2]/a/text()"):
            return tr.xpath("//tr/td[2]/a/text()").extract_first()
        elif self._is_valid_xpath(content, "//tr/td[2]/b/a/text()"):
            return tr.xpath("//tr/td[2]/b/a/text()").extract_first()

    def _is_valid_xpath(self, content, xpath):

        import lxml.html as PARSER
        root = PARSER.fromstring(content)
        if root.xpath(xpath):
            return True
        return False

    def _find_state_short_name(self, state):
        names = self._state_short_names()
        return names[state]

    def _state_short_names(self):

        return {
            "California": "CA",
            "Texas": "TX",
            "Florida": "FL",
            "Colorado": "CO",
            "Arizona": "AZ",
            "North Carolina": "NC",
            "Illinois": "IL",
            "Washington": "WA",
            "Georgia": "GA",
            "Virginia": "VA",
            "Michigan": "MI",
            "New Jersey": "NJ",
            "Ohio": "OH",
            "Tennessee": "TN",
            "Connecticut": "CT",
            "Kansas": "KS",
            "Massachusetts": "MA",
            "Missouri": "MO",
            "New York": "NY",
            "Oregon": "OR",
            "Alabama": "AL",
            "Indiana": "IN",
            "Louisiana": "LA",
            "Nevada": "NV",
            "Oklahoma": "OK",
            "Utah": "UT",
            "Iowa": "IA",
            "Minnesota": "MN",
            "Pennsylvania": "PA",
            "South Carolina": "SC",
            "Wisconsin": "WI",
            "Kentucky": "KY",
            "Nebraska": "NE",
            "New Mexico": "NM",
            "Alaska": "AK",
            "Arkansas": "AR",
            "District of Columbia": "DC",
            "Hawai'i": "HI",
            "Idaho": "ID",
            "Maryland": "MD",
            "Mississippi": "MS",
            "Montana": "MT",
            "North Dakota": "ND",
            "New Hampshire": "NH",
            "Rhode Island": "RI",
            "South Dakota": "SD",
            "Delaware": "DE",
            "Maine": "ME",
            "Vermont": "VT",
            "West Virginia": "WV",
            "Wyoming": "WY",
        }

