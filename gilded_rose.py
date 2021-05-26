# -*- coding: utf-8 -*-
from abc import abstractmethod

MAX_QUALITY: int = 50


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_inventory(self):
        item: Item
        for item in self.items:
            item.update()


class Item:
    sell_in: int
    quality: int

    def __init__(self, sell_in, quality):
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s" % (self.sell_in, self.quality)

    @abstractmethod
    def update(self):
        pass

    @staticmethod
    def create_normal_item(sell_in, quality):
        return NormalItem(sell_in, quality)

    @staticmethod
    def create_sulfuras(sell_in, quality):
        return Sulfuras(sell_in, quality)

    @staticmethod
    def create_aged_brie(sell_in, quality):
        return AgedBrie(sell_in, quality)

    @staticmethod
    def create_backstage_passes(sell_in, quality):
        return BackstagePasses(sell_in, quality)

    @staticmethod
    def create_conjured(sell_in, quality):
        return Conjured(sell_in, quality)


class NormalItem(Item):
    def update(self):
        self.sell_in -= 1
        if self.sell_in > 0:
            self.quality -= 1
        else:
            self.quality -= 2
        if self.quality < 0:
            self.quality = 0


class Sulfuras(Item):
    def update(self):
        pass


class AgedBrie(Item):
    def update(self):
        self.sell_in -= 1
        if self.sell_in > 0:
            self.quality += 1
        else:
            self.quality += 2
        if self.quality > MAX_QUALITY:
            self.quality = MAX_QUALITY


class BackstagePasses(Item):
    def update(self):
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


class Conjured(Item):
    def update(self):
        self.sell_in -= 1
        self.quality -= 2
