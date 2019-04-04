chars = set(sentence)
numbers = [sentence.count(c) for c in chars]
char_frequency = list(zip(chars, numbers))
char_frequency.sort(key=lambda item: item[1], reverse=True)
print(char_frequency[0])
