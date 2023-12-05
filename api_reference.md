# WordPaths API Reference #


Wordpaths consists of two classes: `WordGraph` and `WordPath`.

### `WordGraph` ###

The `WordGraph` class represents relationships that words have to each other. Each word is a key which maps to an array containing all of its neighbooring words--words which can be creating by only adding, subtracting, or changes one letter.



```py
class WordGraph:
    def __init__(self, dictionary: list[str]) -> None:
        self.dictionary = dictionary   # list[str]
        self.graph = defaultdict(set)  # dict[str, set[str]]
```

WordGraph builds itself on initialization using the words in `dictionary`:


```py
WordGraph.build_from_file(cls, path: str) -> "WordGraph"
```
Returns the contents of a file split on newlines and striped. This function should be used initialize a WordGraph directly from a file:


```py
WordGraph.__get_variations(cls, word: str) -> list[str]
```
`__get_variations` is a private class function returns all variation patterns of a given word. A variation pattern is defined as any string of letters that is only one change away from the origin word. A change is either an added letter, a subtracted letter, or a replaced letter. Underscores in variation patterns represent wildcards and allow for multiple words to match to a single pattern.


Whene a WordGraph is initialized, a temporary variations graph is created, mapping variations to all words that they can represent:

```py
{
    'fl_p' : ['flip', 'flop', 'flap'],
    'lip'  : ['lip']
}

```

### `WordPath` ###

```py
class WordPath:
    def __init__(self, start_word: str, end_word: str, graph: WordGraph) -> None:
        self.start_word = start_word.lower()  # str
        self.end_word = end_word.lower()      # str
        self.paths = dict()                   # dict[str, str]
        self.paths[start_word] = start_word
        self.queue = deque()                  # deque[str]
        self.queue.append(start_word)
        self.graph = graph                    # WordGraph

```

The `WordPath` traverses a `WordGraph` using a bredth-first search. Multiple wordpaths can share a WordGraph. Since WordPaths search one step at a time, it is possible to improve the efficieny of a search by using two WordPaths: one starting on the desired start and end word and the other starting on the desired end word and ending on the desired start word. When both WordPaths contain a shared word, a path can be created.

