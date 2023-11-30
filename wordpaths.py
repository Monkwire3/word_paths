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

def one_change_away(start_word):
    adjacent_words = []
    with open("./words.txt", "r") as f:
        all_words = f.read().split("\n")
        for i, word in enumerate(all_words):

            print(f"checking word ({i}/{len(all_words)})")
            if is_one_change_away(start_word, word):
                adjacent_words.append(word)

    return adjacent_words


def main():
    word = "cake"
    print(one_change_away(word))
main()

