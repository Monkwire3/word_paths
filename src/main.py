from collections import defaultdict


def is_one_change_away(a, b):
    diff_count = 0

    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] != b[i]:
                if diff_count:
                    return False

                diff_count += 1

    elif len(a) == len(b) + 1:
        idx_a = 0
        idx_b = 0

        while len(a) > max([idx_a, idx_b]) and idx_b < len(b):
            if a[idx_a] != b[idx_b]:
                if diff_count:
                    return False

                diff_count += 1
                idx_b -= 1

            idx_a += 1
            idx_b += 1


    elif len(b) == len(a) + 1:
        idx_a = 0
        idx_b = 0

        while len(b) > max([idx_a, idx_b]) and idx_a < len(a):
            if a[idx_a] != b[idx_b]:
                if diff_count:
                    return False

                diff_count += 1
                idx_a -= 1
            idx_a += 1
            idx_b += 1
    else:
        return False

    return True






def bfs(start_word, end_word, words):
    queue = [[start_word]]
    avoid = set()


    while len(queue):
        visiting = queue.pop(0)
        avoid.add(visiting[-1])

        if visiting[-1] == end_word:
            return visiting

        for word in get_adjacent(visiting[-1], words, avoid):
            if word not in visiting:
                queue.append(visiting + [word])


def get_adjacent(start_word, words, avoid_words=set()):
    avoid_words.add(start_word)
    adjacent_words = []
    for i, word in enumerate(words):

        if word not in avoid_words and is_one_change_away(start_word, word):
            adjacent_words.append(word)

    return adjacent_words


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


def main():
    words = []
    with open("./words.txt", "r") as f:
        words = f.read().split("\n")

    graph = build_graph(words)
    print(find_path("book", "nook", words, graph))
    print(find_path("run", "runt", words, graph))
    print(find_path("brunt", "front", words, graph))
    print(find_path("choose", "coke", words, graph))
    print(find_path("zebra", "coke", words, graph))

main()
