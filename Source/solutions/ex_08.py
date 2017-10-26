def count_words(words, min_word_length):
    counter = 0
    for word in words:
        if len(word) >= min_word_length and 'e' in word:
            counter += 1
    return counter


print(count_words(['Emanuel', 'John', 'Ale'], 4))