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

def build_graph():
    graph = dict()

    with open("./words.txt", "r") as f:
        all_words = f.read().split("\n")
        for i, word in enumerate(all_words):
            print(f"building graph: {i}/{len(all_words)}")
            graph[word] = get_adjacent(word, all_words)



    return graph


def get_adjacent(start_word, words, avoid_words=set()):
    avoid_words.add(start_word)
    adjacent_words = []
    for i, word in enumerate(words):

        if word not in avoid_words and is_one_change_away(start_word, word):
            adjacent_words.append(word)

    return adjacent_words



# def find_word(word, goal, visited, graph):
#     if word == goal:
#         return [word]
#
#
#     visited.add(word)
#
#     if len(list(filter(lambda x: x not in visited, graph[word]))):
#         return [word] + [min(map(lambda x: find_word(x, goal, visited, graph), filter(lambda y: y not in visited, graph[word])), key=len)]
#
#     return []



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





def main():
    words = []
    with open("./words.txt", "r") as f:
        words = f.read().split("\n")
    # graph = build_graph()

    # start_words = ["one", "floss"]
    # end_words = ["boney", "brass"]
    # for i in range(len(start_words)):
    #     s = start_words[i]
    #     e = end_words[i]
    #     print("=" * 10)
    #     print("start: ", s, "end: ", e)
    #     print(bfs(s, e, words))
    #     print("=" * 10)

main()
