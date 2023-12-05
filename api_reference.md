# WordPaths API Reference #


Wordpaths consists of two classes: `WordGraph` and `WordPath`.

### `WordGraph` ###

The `WordGraph` class represents the relationships that words have to each other. Each word is a key which maps to an array containing all of its neighbooring words--words which can be creating by only adding, subtracting, or changes one letter.


WordGraph builds itself on initialization using the words in `dictionary`:

```py
class WordGraph:
    def __init__(self, dictionary: list[str]) -> None:
        self.dictionary = dictionary   # list[str]
        self.graph = defaultdict(set)  # dict[str, set[str]]

        variations_graph = defaultdict(list)

        for _, word in enumerate(self.dictionary):
            word = word.strip().lower()
            variations = self.__get_variations(word)
            for v in variations:
                variations_graph[v].append(word)


        for _, word in enumerate(self.dictionary):
            for variation in self.__get_variations(word.strip().lower()):
                for neighbor in variations_graph[variation]:
                    if neighbor != word:
                        self.graph[word].add(neighbor)
                        self.graph[neighbor].add(word)

```



```py
WordGraph.build_from_file(cls, path: str) -> "WordGraph"
```
Returns the contents of a file split on newlines and striped. This function should be used initialize a WordGraph directly from a file:


```py
WordGraph.__get_variations(cls, word: str) -> list[str]
```



### `class WordPath`{:.python} ###

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

The `WordPath` traverses a `WordGraph` using a bredth-first search.
