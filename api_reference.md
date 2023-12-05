# WordPaths API Reference #


Wordpaths consists of two classes: `WordGraph` and `WordPath`.

### `WordGraph` ###
`class WordGraph: # dict[str, list[str]]`
The `WordGraph` class represents the relationships that words have to each other. Each word is a key which maps to an array containing all of its neighbooring words--words which can be creating by only adding, subtracting, or changes one letter.

`WordGraph.__init__(self, dictionary: list[str])`
WordGraph builds itself on initialization using the words in `dictionary`.

`WordGraph.build_from_file(cls, path: str)`
Returns the contents of a file split on newlines and striped. This function should be used initialize a WordGraph directly from a file:
`graph = WordGraph.build_from_file(file_path)`



### `WordPath` ###
