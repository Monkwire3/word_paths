from collections import defaultdict

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
