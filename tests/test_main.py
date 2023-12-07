import unittest
from src.main import  WordGraph

test_dict = ["bite", "bike", "book", "bike", "hike", "like", "lice", "vice" , "mice", "lice", "dice", "rice", "look", "nook", "cook", "hook", "hock", "hick", "biker", "bikers"]
graph = WordGraph(dictionary=test_dict)

class FindWordPathTests(unittest.TestCase):
    def test_two_word_path(self):
        assert(graph.get_path(start_word='bite', end_word='bike') == ['bite', 'bike'])

    def test_long_word_path(self):
        assert(graph.get_path(start_word='bite', end_word='vice') == ["bite", "bike", "like", "lice", "vice"])

    def test_path_with_letter_addition(self):
        assert(graph.get_path(start_word='bike', end_word='bikers') == ['bike', 'biker', 'bikers'])

    def test_path_with_letter_subtraction(self):
        assert(graph.get_path(start_word='bikers', end_word='bike') == ['bikers', 'biker', 'bike'])


    def test_one_word_path(self):
        assert(graph.get_path(start_word='bite', end_word='bite') == ['bite'])

    def test_path_with_empty_graph(self):
        empty_graph = WordGraph(dictionary=[])
        assert(empty_graph.get_path(start_word='bite', end_word='bike') == [])
