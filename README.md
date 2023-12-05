# WordPaths
## Intro ##
WordPaths generates the shortest path between two words. Each path is guaranteed to use only words from a given dictionary.


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


You can create a `WordGraph` from an array:
```py
from wordpaths.src.main import WordGraph, WordPath

word_dict = ['bird', 'bread', 'bard', 'bad', 'bead', 'bald', 'ball']
word_graph = WordGraph(dictionary=word_dict)
word_path = WordPaths(start_word="bird", end_word='bald', graph=word_graph)

word_path.get_path()
# ['bird', 'bard', 'bald']
```

You can create a word_graph directly from a file:
```py
word_graph = WordGraph().build_file("/words.txt")
```


