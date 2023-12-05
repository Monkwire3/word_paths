import sys
import os
import argparse
import time
from collections import defaultdict, deque



class WordGraph:
    """
    WordGraph.dictionary : list[str]
    WordGraph.graph      : dict[str, set[str]]

    """
    def __init__(self, dictionary: list[str]) -> None:
        self.dictionary = dictionary
        self.graph = defaultdict(set)

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

    @classmethod
    def build_from_file(cls,  path: str) -> "WordGraph":
        with open(path, "r") as f:
            return cls(f.read().splitlines())


    @classmethod
    def __get_variations(cls, word: str) -> list[str]:
        variations = []

        for i in range(len(word)):
            variations.append(word[:i] + "_" + word[i:])
            variations.append(word[:i] + "_" + (word[i + 1:] if i < len(word) - 1 else ""))
        variations.append(word + "_")

        return variations



class WordPath:
    def __init__(self, start_word: str, end_word: str, graph: WordGraph) -> None:
        self.start_word = start_word.lower()  # str
        self.end_word = end_word.lower()      # str
        self.paths = dict()                   # dict[str, str]
        self.paths[start_word] = start_word
        self.queue = deque()                  # deque[str]
        self.queue.append(start_word)
        self.graph = graph                    # WordGraph

    def find_one_step(self) -> None:
        current = self.queue.popleft()

        for neighbor in self.graph.graph[current]:
            if neighbor != current and neighbor not in self.paths:
                self.paths[neighbor] = current
                self.queue.append(neighbor)

    def get_path(self) -> list[str]:
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

    print("Building graph from ", args.path)


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

            path = WordPath(word_1, word_2, graph)
            print(path.paths)
            print(path.get_path())


            if args.benchmark:
                end_time = time.perf_counter_ns()

            print("=" * os.get_terminal_size(0)[0])
            print(" -> ".join(path.get_path()))
            print_if(f"Found in {(end_time - start_time) // 10 ** 6} milliseconds.", args.benchmark)
            print("=" * os.get_terminal_size(0)[0])
        elif len(user_input) and user_input[0] in ["quit", "exit"]:
            print("Exiting...")
            break
        else:
            print(f"Invalid input:  '{' '.join(user_input)}'")


main()
