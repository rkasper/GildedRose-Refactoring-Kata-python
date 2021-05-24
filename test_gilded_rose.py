# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_we_can_run_tests(self):
        """Ensure that we can run unit tests."""
        self.assertTrue(True)

    def test_system_lowers_both_values_for_every_item(self):
        """Test the basics.

        - All items have a SellIn value which denotes the number of days we have to sell the item
	    - All items have a Quality value which denotes how valuable the item is
	    - At the end of each day our system lowers both values for every item
	    """
        items = [Item("foo", 7, 11), Item("bar", 23, 42)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        self.assertEqual(6, items[0].sell_in)
        self.assertEqual(10, items[0].quality)
        self.assertEqual("bar", items[1].name)
        self.assertEqual(22, items[1].sell_in)
        self.assertEqual(41, items[1].quality)

    def test_quality_degrades_twice_as_fast(self):
        """Once the sell by date has passed, Quality degrades twice as fast"""
        items = [Item("foo", 0, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)


if __name__ == '__main__':
    unittest.main()
