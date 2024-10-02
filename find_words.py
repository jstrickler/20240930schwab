FIRST_LETTER = 'q'

found_words = []
with open('DATA/words.txt') as words_in:
    for raw_word in words_in:
        word = raw_word.rstrip()
        if word.startswith('q') and len(word) > 12:
            found_words.append(word)

print(f"{found_words[-10:] = }")
print(f"{len(found_words) = }")
