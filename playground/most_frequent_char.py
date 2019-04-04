# Find the most frequent character in this sentence
sentence = "This is one of common interview questions."

# Solution 1
char_frequency1 = {c: sentence.count(c) for c in set(sentence)}
print(sorted(char_frequency1.items(), key=lambda kv: kv[1], reverse=True)[0])

# Solution 2
chars = set(sentence)
numbers = [sentence.count(c) for c in chars]
char_frequency2 = list(zip(chars, numbers))
char_frequency2.sort(key=lambda item: item[1], reverse=True)
print(char_frequency2[0])
