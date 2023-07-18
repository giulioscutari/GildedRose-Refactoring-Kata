# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    """GildedRose tests.""""
    
    def test_quality_decreases(self):
        """Test the quality of an object decreases."""
        items = [Item("item", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].quality)
    
    def test_sellIn_decreases(self):
        """Test the sellIn value of an object decreases."""
        items = [Item("item", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].sell_in)

    def test_quality_increases(self):
        """Test the quality of an object increases."""
        items = [Item("Aged Brie", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(11, items[0].quality)
        
if __name__ == '__main__':
    unittest.main()
