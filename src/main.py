import sys
import os
import argparse
import time
from collections import defaultdict, deque
from typing import DefaultDict


def build_graph(words) -> DefaultDict[str, set[str]]:
    def get_variations(word) -> list[str]:
        variations = []

        for i in range(len(word)):
            variations.append(word[:i] + "_" + word[i:])
            variations.append(word[:i] + "_" + (word[i + 1:] if i < len(word) - 1 else ""))
        variations.append(word + "_")

        return variations

    variations_graph = defaultdict(list)

    for i, word in enumerate(words):
        variations = get_variations(word)
        for v in variations:
            variations_graph[v].append(word)

    graph = defaultdict(set)
    for i, word in enumerate(words):
        for variation in get_variations(word):
            for neighbor in variations_graph[variation]:
                if neighbor != word:
                    graph[word].add(neighbor)
                    graph[neighbor].add(word)

    return graph


class WordPath:
    def __init__(self, start_word: str, end_word: str, graph: DefaultDict[str, set[str]]) -> None:
        self.start_word = start_word
        self.end_word = end_word
        self.paths = dict()
        self.paths[start_word] = start_word
        self.queue = deque()
        self.queue.append(start_word)
        self.graph = graph

    def find_one_step(self) -> None:
        current = self.queue.popleft()

        for neighbor in self.graph[current]:
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



def set_up_args() -> argparse.Namespace:
    sys.stdout.flush()
    parser = argparse.ArgumentParser(prog="findpath", description="Finds the shortest path between two words")
    parser.add_argument('-p', '--path')
    parser.add_argument('-b', '--buffer')
    parser.add_argument('-i', '--interactive', action='store_true')


    args = parser.parse_args()
    return args


def main():
    args = set_up_args()
    PATH = args.path if args.path and os.path.isfile(args.path) else "/usr/share/dict/words"


    words = []
    with open(PATH, "r") as f:
        words = f.read().split("\n")

    print(f"Building graph from {PATH}")
    graph = build_graph(words)


    if args.interactive:
        print("Loading interactive mode...")
        user_input = ""
        while user_input not in  ["quit", "exit"]:
            user_input = input("Enter two words, separated by a space: \n").split(" ")
            if len(user_input) == 2:
                word_1, word_2 = user_input
                start_time = time.perf_counter_ns()
                path = WordPath(word_1, word_2, graph).get_path()
                end_time = time.perf_counter_ns()
                print("=" * os.get_terminal_size(0)[0])
                print(path)
                print("Found in", (end_time - start_time) // 10 ** 6, "milliseconds.")
                print("=" * os.get_terminal_size(0)[0])


main()
