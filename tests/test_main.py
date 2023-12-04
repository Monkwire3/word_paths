import unittest
from src.main import WordPath, WordGraph

test_dict = ["bite", "bike", "book", "bike", "hike", "like", "lice", "vice" , "mice", "lice", "dice", "rice", "look", "nook", "cook", "hook", "hock", "hick", "biker", "bikers"]
graph = WordGraph(dictionary=test_dict)

class FindWordPathTests(unittest.TestCase):
    def test_two_word_path(self):
        word_path = WordPath(start_word="bite", end_word="bike", graph=graph)
        assert(word_path.get_path() == ["bite", "bike"])

    def test_long_word_path(self):
        word_path = WordPath(start_word="bite", end_word="vice", graph=graph)
        assert(word_path.get_path() == ["bite", "bike", "like", "lice", "vice"])

    def test_path_with_letter_addition(self):
        word_path = WordPath(start_word="bike", end_word="bikers", graph=graph)
        assert(word_path.get_path() == ["bike", "biker", "bikers"])

    def test_path_with_letter_subtraction(self):
        word_path = WordPath(start_word="bikers", end_word="bike", graph=graph)
        assert(word_path.get_path() == ["bikers", "biker", "bike"])

