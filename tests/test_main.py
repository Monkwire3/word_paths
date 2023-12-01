import sys
import os
import src
import unittest
from src.main import bfs


class FindWordPathTests(unittest.TestCase):
    def test_find_word_path(self):
        word_bank = ["bite", "bike", "book", "bike", "hike", "like", "lice", "vice" , "mice", "lice", "dice", "rice", "look", "nook", "cook", "hook", "hock", "hick"]

        assert(bfs("bike", "lice", word_bank) == ["bike", "like", "lice"])

        assert(bfs("bike", "bike", word_bank) == ["bike"])



