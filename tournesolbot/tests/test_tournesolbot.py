# -*- encoding: utf-8 -*-
import unittest

from tournesolbot.__main__ import get_top_percentage


class TestGetTopPercentage(unittest.TestCase):

    def test_get_top_percentage(self):
        criteria = {'quantile_val': 0.2}
        result = get_top_percentage(criteria)
        self.assertEqual("Top 20%", result)

        criteria = {'quantile_val': 0.01}
        result = get_top_percentage(criteria)
        self.assertEqual("Top 1%", result)

        criteria = {'quantile_val': 0.5}
        result = get_top_percentage(criteria)
        self.assertEqual("Top 50%", result)

        criteria = {'quantile_val': 0.49}
        result = get_top_percentage(criteria)
        self.assertEqual("Top 49%", result)

        criteria = {'quantile_val': 0.8}
        result = get_top_percentage(criteria)
        self.assertEqual("Not in Top 50%", result)

        criteria = {'quantile_val': 0.51}
        result = get_top_percentage(criteria)
        self.assertEqual("Not in Top 50%", result)
