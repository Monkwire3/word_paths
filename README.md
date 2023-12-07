# WordPaths
## Intro ##
WordPaths generates the shortest path between two words, such that a step in the path is both a valid dictionary word, and only one addition, subtraction, or substitution away from the previous step.


For example, the path between "word" and "paths" might look like:

```py
['word', 'ward', 'wars', 'warts', 'parts', 'pats', 'paths']
```

## Getting Started ##
To try out this program, clone the repository:

`git clone https://github.com/Monkwire3/word_paths.git`

From the root of the directory, run the program using:

`python3 src/main.py`

You will need Python version 3.11 or newer to run WordPaths.


## Flags ##
This program can be run with the following flags:

- `-p` or `--path` -- Defines the path that the dictionary is pulled from. The default path is `/usr/share/dict/words`.

- `-b` or `--benchmark` -- Toggles on benchmark mode. In benchmark mode, all operations are timed, and speeds are printed.

To start the program with all flags, run:
`python3 src/main.py -p './words.txt' -b`


## Usage as a Module ##
First, import the `WordGraph` class:

```py
from wordpaths.src.main import WordGraph
```

You can create a `WordGraph` from an array:
```py
word_dict = ['bird', 'bread', 'bard', 'bad', 'bead', 'bald', 'ball']
word_graph = WordGraph(dictionary=word_dict)
```

Or, you can create a `WordGraph` from a file:
```py
word_graph = WordGraph().build_from_file("./words.txt")
```

To find the path between two words in a `WordGraph`, use `get_path()`:
```py
word_graph.get_path(start_word="bird": end_word="bald")
# ['bird', 'bard', 'bald']
```
See the [api reference](https://github.com/Monkwire3/word_paths/blob/main/api_reference.md) for more a more comprehensive guide.
