import unittest
from src.main import find_path, find_path_efficient

WORDBANK = ["bite", "bike", "book", "bike", "hike", "like", "lice", "vice" , "mice", "lice", "dice", "rice", "look", "nook", "cook", "hook", "hock", "hick"]

class FindWordPathTests(unittest.TestCase):

    def test_find_path_same_len_words(self):
        assert(find_path("bike", "lice", WORDBANK) == ["bike", "like", "lice"])
    def test_find_path_same_words(self):
        assert(find_path("bike", "bike", WORDBANK) == ["bike"])

    def test_find_path_same_no_bank(self):
        assert(find_path("bike", "car", WORDBANK) == [])

    def test_find_path_efficient_same_len_words(self):
        assert(find_path_efficient("bike", "lice", WORDBANK) == ["bike", "like", "lice"])
    def test_find_path_efficient_same_words(self):
        assert(find_path_efficient("bike", "bike", WORDBANK) == ["bike"])

    def test_find_path_efficient_same_no_bank(self):
        assert(find_path_efficient("bike", "car", WORDBANK) == [])



