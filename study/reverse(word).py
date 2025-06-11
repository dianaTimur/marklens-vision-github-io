word = input('Enter your a word \n')
print('-' * 20)

list_words = list(word)
list_words.reverse()
print(list_words)
str_words = ''.join(list_words)

print(str_words)

#اختصار كود

words = input('Enter your a words:\t')
print("-" * 15)
print (f'{"".join(list(reversed(words)))}')

