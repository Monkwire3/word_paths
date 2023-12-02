import os
import argparse
import time
from collections import defaultdict, deque
import math

def get_variations(word):
    variations = []

    for i in range(len(word)):
        variations.append(word[:i] + "_" + word[i:])
        variations.append(word[:i] + "_" + (word[i + 1:] if i < len(word) - 1 else ""))
    variations.append(word + "_")

    return variations


def build_graph(words):
    variations_graph = defaultdict(list)

    for word in words:
        variations = get_variations(word)
        for v in variations:
            variations_graph[v].append(word)

    graph = defaultdict(set)
    for word in words:
        for variation in get_variations(word):
            for neighbor in variations_graph[variation]:
                if neighbor != word:
                    graph[word].add(neighbor)
                    graph[neighbor].add(word)

    return graph


def find_path(start_word, end_word, graph):
    paths = dict()
    paths[start_word] = start_word

    queue = deque([start_word])

    while len(queue):
        current = queue.popleft()

        if current == end_word:
            path = [current]

            while path[-1] != start_word:
                path.append(paths[path[-1]])

            return path[::-1]

        for neighbor in graph[current]:
            if neighbor not in paths:
                paths[neighbor] = current
                queue.append(neighbor)

    return []


class WordPath:
    def __init__(self, start_word, end_word, graph) -> None:
        self.start_word = start_word
        self.end_word = end_word
        self.paths = dict()
        self.paths[start_word] = start_word
        self.queue = deque()
        self.queue.append((start_word, 0))
        self.graph = graph

    def find_one_step(self):
        current, depth = self.queue.popleft()

        for neighbor in self.graph[current]:
            if neighbor != current and neighbor not in self.paths:
                self.paths[neighbor] = current
                self.queue.append((neighbor, depth + 1))

    def get_path(self):
        while self.queue:
            self.find_one_step()
            if self.end_word  in self.paths:

                path = [self.end_word]

                while path[-1] != self.start_word:
                    path.append(self.paths[path[-1]])

                return path[::-1]
        return []

def main():
    print("loading...")
    parser = argparse.ArgumentParser(prog="findpath", description="Finds the shortest path between two words")
    parser.add_argument('-p', '--path')
    args = parser.parse_args()

    PATH = "/usr/share/dict/words"

    if args.path:
        if os.path.isfile(args.path):
            PATH = args.path
        else:
            print(f"{args.path} is not a valid file path. Instead using {PATH}.\n")

    words = []
    with open(PATH, "r") as f:
        words = f.read().split("\n")

    graph = build_graph(words)

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
            print("[efficient] Found in", (end_time - start_time) // 10 ** 6, "milliseconds.")
            print("=" * os.get_terminal_size(0)[0])

            word_1, word_2 = user_input
            start_time = time.perf_counter_ns()
            path = find_path(word_1, word_2, graph)
            end_time = time.perf_counter_ns()
            print("=" * os.get_terminal_size(0)[0])
            print(path)
            print("[normal] Found in", (end_time - start_time) // 10 ** 6, "milliseconds.")
            print("=" * os.get_terminal_size(0)[0])

main()
