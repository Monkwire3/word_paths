# word_paths
## Intro ##
WordPaths is a short program that generates the shortest path between two words. Each path is guaranteed to use only words from a given dictionary.


## Getting Started ##
To try out this program yourself, clone the repository:
`git clone https://github.com/Monkwire3/word_paths.git`

From the root of the directory, run the program using:
`python3 src/main.py`

See the [api reference](https://github.com/Monkwire3/word_paths/blob/main/api_reference.md) for additional program information.

## Flags ##
This program can be run witht the following flags:

- `-p` or `--path`: Defines the path that the dictionary is pulled from. By default the path is `/usr/share/dict/words`.

- `-b` or `--benchmark`: Toggles on benchmark data printing.

Exmaple:
    `python3 src/main.py -p './words.txt' -b`

