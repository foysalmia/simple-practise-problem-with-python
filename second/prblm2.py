# given data set

str = "We tried list and we tried dicts also we tried Zen"
words = str.split(" ")
setOfwords = set(words)
count_words = {}
for word in setOfwords:
    count_words[word] = 0

for word in words:
    count_words[word] += 1

for word, value in count_words.items():
    print(word, value)
