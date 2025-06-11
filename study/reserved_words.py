import random
import time

# list of words
words = [
'have', 'that', 'they', 'with', 'this', 'from', 'which', 'would', 'will',
'there',
'make', 'when', 'more', 'other', 'what', 'time', 'about', 'than', 'into',
'could',
'state', 'only', 'year', 'some', 'take', 'come', 'these', 'know', 'like',
'then',
'first', 'work', 'such', 'give', 'over', 'think', 'most', 'even', 'find',
'also',
'after', 'many', 'must', 'look', 'before', 'great', 'back', 'through',
'long',
'where', 'much', 'should', 'well', 'people', 'gouda', 'just', 'because',
'good',
'each', 'those', 'feel', 'seem', 'high', 'place', 'little', 'world',
'very', 'still',
'nation', 'hand', 'life', 'tell', 'write', 'become', 'here', 'show',
'house', 'both',
'between', 'need', 'mean', 'call', 'develop', 'under', 'last', 'right',
'move', 'thing',
'general', 'school', 'never', 'same', 'another', 'begin', 'while',
'number', 'part',
'turn', 'real', 'leave', 'might', 'want', 'point', 'form', 'child',
'small', 'since',
'against', 'late', 'home', 'interest', 'large', 'person', 'open',
'public', 'follow',
'during', 'present', 'without', 'again', 'hold', 'codezilla', 'govern',
'around',
'head', 'consider', 'word', 'program', 'problem', 'however', 'lead',
'system',
'order', 'plan', 'keep', 'face', 'group', 'play', 'stand', 'increase',
'early', 'course', 'change', 'help', 'line', 'possible', 'fact', 'down'
]

random_list = random.randint(0, len(words)-1)
index_list = words[random_list]
function_list = list(index_list)
function_list.reverse()
join_list = "".join(function_list)

print('Welcome to the Reserved Words Game ')
print(f'The reserved word is: {join_list}')
frist_time = time.time()
user_word = input("The word is: ")
secend_time = time.time()

total_time = secend_time - frist_time
print(total_time)

if user_word == index_list and total_time < 5:
    print("You won!")
elif user_word != index_list and total_time > 5:
    print("Wrong word \nYou took too long \nYou lost!")
elif user_word != index_list:
    print('Wrong word \nYou lost! ')
else:
    print('You took too long \nYou lost! ')
