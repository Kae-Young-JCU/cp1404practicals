"""
Word Occurrences
Estimate: 20 minutes
Actual: 28 minutes
"""

text = input("Enter a string: ")
words = text.split(" ")
word_count = {}
max_word_length = 0
for word in words:
    if len(word) > max_word_length:
        max_word_length = len(word)
    try:
        word_count[word] += 1
    except KeyError:
        word_count[word] = 1
sorted_values = sorted(word_count)
print(sorted_values)
for value in sorted_values:
    print(f"{value:{max_word_length}} : {word_count[value]}")

