# -*- coding: utf-8 -*-
MAX_QUALITY: int = 50
SULFURAS: str = "Sulfuras, Hand of Ragnaros"
AGED_BRIE: str = "Aged Brie"
BACKSTAGE_PASSES: str = "Backstage passes to a TAFKAL80ETC concert"
CONJURED: str = "Conjured"


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_inventory(self):
        item: Item
        for item in self.items:
            # Update if the item is a normal item
            if not (item.name == AGED_BRIE or BACKSTAGE_PASSES == item.name or SULFURAS == item.name
                    or CONJURED == item.name):
                item.sell_in -= 1
                if item.sell_in > 0:
                    item.quality -= 1
                else:
                    item.quality -= 2
                if item.quality < 0:
                    item.quality = 0

            # Update if the item is Sulfuras
            if SULFURAS == item.name:
                pass

            # Update if the item is Aged Brie
            if AGED_BRIE == item.name:
                item.sell_in -= 1
                if item.sell_in > 0:
                    item.quality += 1
                else:
                    item.quality += 2
                if item.quality > MAX_QUALITY:
                    item.quality = MAX_QUALITY

            # Update if the item is Backstage Passes
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

            # Update if the item is Conjured
            if CONJURED == item.name:
                item.sell_in -= 1
                item.quality -= 2


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
