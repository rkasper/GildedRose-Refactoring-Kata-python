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
            item.update_if_normal_item()
            item.update_if_sulfuras()
            item.update_if_aged_brie()
            item.update_if_backstage_passes()
            item.update_if_conjured()


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

    def update_if_normal_item(self):
        if not (self.name == AGED_BRIE or BACKSTAGE_PASSES == self.name or SULFURAS == self.name
                or CONJURED == self.name):
            self.sell_in -= 1
            if self.sell_in > 0:
                self.quality -= 1
            else:
                self.quality -= 2
            if self.quality < 0:
                self.quality = 0

    def update_if_sulfuras(self):
        if SULFURAS == self.name:
            pass

    def update_if_aged_brie(self):
        if AGED_BRIE == self.name:
            self.sell_in -= 1
            if self.sell_in > 0:
                self.quality += 1
            else:
                self.quality += 2
            if self.quality > MAX_QUALITY:
                self.quality = MAX_QUALITY

    def update_if_backstage_passes(self):
        # Backstage Passes
        if BACKSTAGE_PASSES == self.name:
            self.sell_in -= 1

            if self.quality < MAX_QUALITY:
                self.quality += 1
                if self.sell_in < 11:
                    if self.quality < MAX_QUALITY:
                        self.quality += 1
                if self.sell_in < 6:
                    if self.quality < MAX_QUALITY:
                        self.quality += 1

            if self.sell_in < 0:
                self.quality = 0

    def update_if_conjured(self):
        if CONJURED == self.name:
            self.sell_in -= 1
            self.quality -= 2
