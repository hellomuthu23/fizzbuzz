#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
from src.main import generate_list


class MyTestCase(unittest.TestCase):

    def test_genlist_length(self):
        self.assertEqual(len(generate_list()), 100)

    def test_genlist_first(self):
        self.assertEqual(generate_list()[0], 1)

    def test_genlist_last(self):
        self.assertEqual(generate_list()[99], 100)