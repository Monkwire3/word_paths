import sys
import os
import argparse
import time
from collections import defaultdict, deque



class WordGraph:
    """A class that represents a mapping of words to their neighbors.

    Constructors:
    build_from_file()

    Attributes:
    graph : dict[str, set[str]]
        map of words to a list of their neighors

    Functions:
    _get_variations():
        Return a list of variation patterns that match the input string.
    get_path():
        Return the shortest path between two words such that each step is a valid word and only one change away from the step before it.
    """

    def __init__(self, dictionary: list[str]) -> None:
        """Construct a WordGraph from a list of strings.

        Parameters:
        dictionary : list[str]
            List of words used to generate the graph
        """

        self.graph = defaultdict(set) # Defaultdict[str, set[str]]

        dictionary = dictionary.copy()

        variations_graph = defaultdict(list)

        for _, word in enumerate(dictionary):
            word = word.strip().lower()
            variations = self._get_variations(word)
            for v in variations:
                variations_graph[v].append(word)


        for _, word in enumerate(dictionary):
            for variation in self._get_variations(word.strip().lower()):
                for neighbor in variations_graph[variation]:
                    if neighbor != word:
                        self.graph[word].add(neighbor)
                        self.graph[neighbor].add(word)

    @classmethod
    def build_from_file(cls,  path: str) -> "WordGraph":
        """Constructor. Build a WordGraph from a file containing strings, separated by newlines.

        Files are expected to contain a list of strings, separated by newlines.

        Parameters:
            path : str
                location of source file
        """

        with open(path, "r") as f:
            return cls(f.read().splitlines())


    @classmethod
    def _get_variations(cls, word: str) -> list[str]:
        """Return a list of variation patterns that match a word.

        Variation patterns are strings which are one addition, subtraction, or substitution different from the input word. Wildcards are reprented by underscores.

        Parameters:
        word : str
            basis for variation patterns

        """

        variations = []

        for i in range(len(word)):
            variations.append(word[:i] + "_" + word[i:])
            variations.append(word[:i] + "_" + (word[i + 1:] if i < len(word) - 1 else ""))
        variations.append(word + "_")

        return variations

    def get_path(self, start_word, end_word) -> list[str]:
        """Return an array representing the shortest path between two words."""
        path = WordPath(start_word=start_word, end_word=end_word, graph=self)
        return path.get_path()





class WordPath:
    """A class that represents a path from a start_word to an end_word.

    A WordPath path is generated by traversing a WordGraph using a breadth-first search.

    Attributes:
    start_word : str
        word that begins a path
    end_word : str
        word that ends a path
    paths : dict[str, str]
        map of words to their preceeding neighbors
    queue : deque[str]
        queue of words that will be visited
    graph : WordGraph
        graph of words that can be traversed to build a WordPath
    """

    def __init__(self, start_word: str, end_word: str, graph: WordGraph) -> None:
        """Construct a WordPath.

        Parameters:
        start_word : str
            word that begins a path
        end_word : str
            word that ends a path
        graph : WordGraph
            graph of words that can be traversed to build a WordPath

        """

        self.start_word = start_word.lower()      # str
        self.end_word = end_word.lower()          # str
        self.paths = dict(start_word=start_word)  # dict[str, str]
        self.queue = deque([start_word])          # deque[str]
        self.graph = graph                        # WordGraph

    def find_one_step(self) -> None:
        """Advance one step in a breadth-first search."""
        current = self.queue.popleft()

        for neighbor in self.graph.graph[current]:
            if neighbor != current and neighbor not in self.paths:
                self.paths[neighbor] = current
                self.queue.append(neighbor)

    def get_path(self) -> list[str]:
        """Return an array with the shortest path between two words."""
        while self.queue:
            self.find_one_step()
            if self.end_word in self.paths:

                path = [self.end_word]

                while path[-1] != self.start_word:
                    path.append(self.paths[path[-1]])

                return path[::-1]
        return []


def print_if(string: str, condition: bool) -> None:
    if condition:
        print(string)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="findpath", description="Finds the shortest path between two words")
    parser.add_argument('-p', '--path', default="/usr/share/dict/words")
    parser.add_argument('-b', '--benchmark', default=False)

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    interactive = sys.stdout.isatty()
    start_time, end_time = 0, 0


    print("Building graph from", args.path)


    if args.benchmark:
        start_time = time.perf_counter_ns()

    graph = WordGraph.build_from_file(args.path)

    if args.benchmark:
        end_time = time.perf_counter_ns()

    print_if(f"Graph built in {(end_time - start_time) // 10 ** 6} milliseconds.", interactive and args.benchmark)

    print("Loading interactive mode...")
    print("Type 'quit' or 'exit' to end program.")
    user_input = ""
    while True:
        user_input = input("Enter two words, separated by a space: \n").split(" ")
        if len(user_input) == 2:
            word_1, word_2 = user_input

            if args.benchmark:
                start_time = time.perf_counter_ns()

            path = graph.get_path(word_1, word_2)

            if args.benchmark:
                end_time = time.perf_counter_ns()

            print("=" * os.get_terminal_size(0)[0])
            print(" -> ".join(path))
            print_if(f"Found in {(end_time - start_time) // 10 ** 6} milliseconds.", args.benchmark)
            print("=" * os.get_terminal_size(0)[0])
        elif len(user_input) and user_input[0] in ["quit", "exit"]:
            print("Exiting...")
            break
        else:
            print(f"Invalid input:  '{' '.join(user_input)}'")

if __name__ == "__main__":
    main()
