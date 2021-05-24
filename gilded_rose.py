# -*- coding: utf-8 -*-
MAX_QUALITY = 50
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE = "Aged Brie"


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        item: Item
        for item in self.items:
            self.handle_if_normal_item(item)
            self.handle_if_sulfuras(item)
            self.handle_if_aged_brie(item)
            self.handle_if_backstage_passes(item)

    @staticmethod
    def handle_if_normal_item(item):
        if not (item.name == AGED_BRIE or BACKSTAGE_PASSES == item.name or SULFURAS == item.name):
            item.sell_in -= 1
            if item.sell_in > 0:
                item.quality -= 1
            else:
                item.quality -= 2
            if item.quality < 0:
                item.quality = 0

    @staticmethod
    def handle_if_sulfuras(item):
        if SULFURAS == item.name:
            pass

    @staticmethod
    def handle_if_aged_brie(item):
        if AGED_BRIE == item.name:
            item.sell_in -= 1
            if item.sell_in > 0:
                item.quality += 1
            else:
                item.quality += 2
            if item.quality > MAX_QUALITY:
                item.quality = MAX_QUALITY

    @staticmethod
    def handle_if_backstage_passes(item):
        # Backstage Passes
        if BACKSTAGE_PASSES == item.name:
            item.sell_in -= 1

            if item.quality < MAX_QUALITY:
                item.quality += 1
                if item.sell_in < 11:
                    if item.quality < MAX_QUALITY:
                        item.quality += 1
                if item.sell_in < 6:
                    if item.quality < MAX_QUALITY:
                        item.quality += 1

            if item.sell_in < 0:
                item.quality = 0


class Item:
    name: str
    sell_in: int
    quality: int

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
