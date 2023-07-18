# -*- coding: utf-8 -*-

class GildedRose(object):

    quality_changes_dict = {
        "Aged Brie": 1,
        "Backstage passes to a TAFKAL80ETC concert": 0,
    }
    def __init__(self, items):

        self.item_handlers = []
        for i in items:
            if i.name == "Aged Brie":
                self.item_handlers.append(
                    ItemHandler(item, 1)
                )

    def update_item_quality(self, item):
        """Update single object quality."""
        if item.quality == 50 or "Sulfuras, Hand of Ragnaros" in item.name or item.quality == 0:
            return
        if item.name in quality_changes_dict:
            item.quality += self.quality_changes_dict[item.name]
    
    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemHandler:
    
    def __init__(self, item; quality_change):
        self.item = item
        self.quality_change = quality_change

    def update_item(self):
        self.item.quality += self.quality_change
        self.sell_in -= 1
        

class BackStagePassHandler(ItemHandler):
    pass
