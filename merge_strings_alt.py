def merge_strings(word_one, word_two):
    new_word = []
    if len(word_one) > len(word_two):
        biggest_word = len(word_one)
        lowest_word = len(word_two)
    if len(word_two) >= len(word_one):
        biggest_word = len(word_two)
        lowest_word = len(word_one)

    for i in range(lowest_word):
        new_word.append(word_one[i])
        new_word.append(word_two[i])

    if biggest_word > lowest_word:
        new_word.append(word_one[lowest_word:] if len(word_one) > len(word_two) else word_two[lowest_word:])
    return "".join(new_word)


if __name__ == "__main__":
    input_word_one = input("word1: ")
    input_word_two = input("word2: ")
    final_word = merge_strings(input_word_one, input_word_two)
    print(final_word)

