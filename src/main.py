import datetime
from collections import defaultdict
import math

def get_variations(word):
    variations = []

    for i in range(len(word)):
        variations.append(word[:i] + "_" + word[i:])
        variations.append(word[:i] + "_" + (word[i + 1:] if i < len(word) - 1 else ""))
    variations.append(word + "_")

    return variations



def build_graph(words):
    graph = defaultdict(list)

    for word in words:
        variations = get_variations(word)
        for v in variations:
            graph[v].append(word)

    return graph


def find_path(start_word, end_word, dictionary, graph=None):
    if not graph:
        graph = build_graph(dictionary)
    paths = dict()
    paths[start_word] = start_word
    avoid = set()

    queue = [start_word]

    while len(queue):
        current = queue.pop(0)
        avoid.add(current)

        if current == end_word:
            path = [current]
            prev = paths[end_word]
            if prev != current:
                path.append(prev)

            while prev != start_word:
                prev = paths[prev]
                path.append(prev)

            return path[::-1]

        variations = get_variations(current)
        for variation in variations:
            for neighbor in graph[variation]:
                if neighbor not in avoid:
                    if neighbor not in paths:
                        paths[neighbor] = current
                    queue.append(neighbor)

    return []

def path_overlap(path_1, path_2):
    overlap = ""
    min_steps_seen = math.inf

    for k_1 in path_1:
        v_1 = path_1[k_1]
        if k_1 in path_2:
            v_2 = path_2[k_1]
            steps = v_1[1] + v_2[1]
            if steps < min_steps_seen:
                overlap = k_1


    return overlap



def find_path_efficient(start_word, end_word, dictionary, graph=None):
    if not graph:
        graph = build_graph(dictionary)
    start_to_end_paths = dict()
    start_to_end_paths[start_word] = (start_word, 0)
    start_to_end_avoid = set()

    end_to_start_paths = dict()
    end_to_start_paths[end_word] = (end_word, 0)
    end_to_start_avoid = set()

    start_to_end_queue = [start_word]
    end_to_start_queue = [end_word]

    while len(start_to_end_queue) and len(end_to_start_queue):
        start_to_end_current = start_to_end_queue.pop(0)
        end_to_start_current = end_to_start_queue.pop(0)


        if start_to_end_current == end_word:
            path = [start_to_end_current]
            prev = start_to_end_paths[end_word][0]
            if prev != start_to_end_current:
                path.append(prev)

            while prev != start_word:
                prev = start_to_end_paths[prev][0]
                path.append(prev)

            return path[::-1]


        if end_to_start_current == start_word:
            path = [end_to_start_current]
            prev = end_to_start_paths[start_word][0]
            if prev != end_to_start_current:
                path.append(prev)

            while prev != end_word:
                prev = end_to_start_paths[prev][0]
                path.append(prev)

            return path[::]


        overlap_word = path_overlap(start_to_end_paths, end_to_start_paths)
        if len(overlap_word):
            path = [overlap_word]
            prev = start_to_end_paths[overlap_word][0]

            if overlap_word != prev:
                path.append(prev)

            while prev != start_word:
                prev = start_to_end_paths[prev][0]
                path.append(prev)

            path.reverse()

            nxt = end_to_start_paths[overlap_word][0]
            path.append(nxt)

            while nxt != end_word:
                nxt = end_to_start_paths[nxt][0]
                path.append(nxt)

            return path

        start_to_end_variations = get_variations(start_to_end_current)
        for variation in start_to_end_variations:
            for neighbor in graph[variation]:
                if neighbor not in start_to_end_avoid:
                    if neighbor not in start_to_end_paths:
                        start_to_end_paths[neighbor] = (start_to_end_current, start_to_end_paths[start_to_end_current][1]+ 1)

                    start_to_end_queue.append(neighbor)


        end_to_start_variations = get_variations(end_to_start_current)
        for variation in end_to_start_variations:
            for neighbor in graph[variation]:
                if neighbor not in end_to_start_avoid:
                    if neighbor not in end_to_start_paths:
                        end_to_start_paths[neighbor] = (end_to_start_current, end_to_start_paths[end_to_start_current][1]+ 1)
                    end_to_start_queue.append(neighbor)


    return []



def main():
    words = []
    with open("./words.txt", "r") as f:
        words = f.read().split("\n")

    graph = build_graph(words)
    start_time = datetime.datetime.now()
    print(find_path_efficient("book", "nook", words, graph))
    print(find_path_efficient("run", "runt", words, graph))
    print(find_path_efficient("brunt", "front", words, graph))
    print(find_path_efficient("choose", "coke", words, graph))
    print(find_path_efficient("zebra", "coke", words, graph))
    end_time = datetime.datetime.now()
    print("time efficient: ", end_time - start_time)


    start_time = datetime.datetime.now()
    print(find_path("book", "nook", words, graph))
    print(find_path("run", "runt", words, graph))
    print(find_path("brunt", "front", words, graph))
    print(find_path("choose", "coke", words, graph))
    print(find_path("zebra", "coke", words, graph))
    end_time = datetime.datetime.now()
    print("time normal: ", end_time - start_time)

main()
