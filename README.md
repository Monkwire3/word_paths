# WordPaths
## Intro ##
WordPaths generates the shortest path between two words, such each step in the path is both a valid dictionary word and only one addition, subtraction, or substitution different fromn the previous step.

For example the path between "word" and "path" might look like:

```py
['word', 'wore', 'ware', 'pare', 'pate', 'path']
```

## Getting Started ##
To try out this program, clone the repository:

`git clone https://github.com/Monkwire3/word_paths.git`

From the root of the directory, run the program using:

`python3 src/main.py`

See the [api reference](https://github.com/Monkwire3/word_paths/blob/main/api_reference.md) for additional information.

## Flags ##
This program can be run with the following flags:

- `-p` or `--path` : Defines the path that the dictionary is pulled from. By default the path is `/usr/share/dict/words`.

- `-b` or `--benchmark` : Toggles on benchmark mode. In benchmark mode, all operations are timed, and speeds are printed.

To start the program with all flags, run:
`python3 src/main.py -p './words.txt' -b`


## Usage as a Module ##
First, import the WordGraph:

```py
from wordpaths.src.main import WordGraph, WordPath
```

You can create a `WordGraph` from an array:
```py
word_dict = ['bird', 'bread', 'bard', 'bad', 'bead', 'bald', 'ball']
```

Or, you can create a `WordGraph` from a file:
```py
word_graph = WordGraph().build_file("/words.txt")
```

To find the path between two words in a WordGraph, use `get_path()`:
```py
word_graph.get_path(start_word="bird": end_word="bald")
# ['bird', 'bard', 'bald']
```
