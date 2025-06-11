# print('Make the following numbers negative.')
# nums = [2, 29, 4, 8, 42, 55, 70, 74, 78, 27]
# negative_numbers = [-negative for negative in nums]
# print(negative_numbers)


# print('-' *  50)

# print('Create a new list with the square of the numbers inthe given list.')
# nums = [2, 29, 4, 8, 42, 55, 70, 74, 78, 27]
# square_numbers = [squera**2 for squera in nums ]
# print(square_numbers)

# print('-' *  50)

# print('create a new list with the scores as percent and eachscore in the format of 88%')

# scores = [75, 87, 93, 98, 82, 67, 91, 88]
# format_scores = [f'{format}%' for format in scores]
# print(format_scores)

# print('-' * 50)

# print('Make a list with all the items in the following list in lowercase')

# fruits = ["APPLE", "ORANGE", "BANANA", "PEAR", "MANGO"]
# lower_fruits = [fruit.lower() for fruit in fruits]
# print(lower_fruits)

# print('-' * 50)

# print('Write code to find the sum of the even numbers in the list.')

# nums = [2, 29, 4, 8, 42, 55, 70, 74, 78, 27]
# even_numbers = [even for even in nums if even % 2 == 0]
# print(even_numbers)

# print('-'  * 50)

# print('Make a new list with prices in the following form .$10.99')

# prices = [10.99, 20.99, 30.99, 40.99, 50.99]

# prices_numbers = [f'${price}' for price in prices]
# print(prices_numbers)


# print("-" * 20)

# '''Write code to find the sum of numbers that are divisible by 3 
# and between 20 and 140 then print the numbers separated by a comma.'''

# divisible_3 = [i for i in range (20,141) if i % 3 == 0]

# print(f'The list of number divisible 3 is : {divisible_3}')
# print(f'The sum of divisible 3 is : {sum(divisible_3):,}')


# print('-' * 20)
# '''Make a List with 20 random numbers between 100 and 1000.'''

# import random

# numbers = [random.randint(100,1_000) for _ in range (21)]
# print(numbers)

# print('-' * 20) 

# '''Make list with 100 random numbers between 100 and 10,000 that are divisible by 3 and 5 '''

# random_number = [random.randint(100,10_000) for _ in range(100)]

# divisible_3_5 = [x for x in random_number if x % 3 == 0 or x % 5 == 0]


# print(f'The number divible 3 and 5 in {divisible_3_5 }')

# print('-' * 20)

# '''Modify this list of words to make All words are uppercase.'''
# # list of words
# words = [
# 'have', 'that', 'they', 'with', 'this', 'from', 'which', 'would', 'will', 'there',
# 'make', 'when', 'more', 'other', 'what', 'time', 'about', 'than', 'into', 'could',
# 'state', 'only', 'year', 'some', 'take', 'come', 'these', 'know', 'like', 'then',
# 'first', 'work', 'such', 'give', 'over', 'think', 'most', 'even', 'find', 'also',
# 'after', 'many', 'must', 'look', 'before', 'great', 'back', 'through', 'long',
# 'where', 'much', 'should', 'well', 'people', 'gouda', 'just', 'because', 'good',
# 'each', 'those', 'feel', 'seem', 'high', 'place', 'little', 'world', 'very', 'still',
# 'nation', 'hand', 'life', 'tell', 'write', 'become' ]

# uppercase_words = [word.upper() for word in words ]

# print(uppercase_words)

# print('-' * 20)

# # Edit words list to gain the following outputs.



# words = [["Hello", "from", "Codezilla"], ["Python", "Course", "is", "awesome"],
# ["I", "enjoy", "learning", "Python", "with", "Codezilla"]]

# normal_words = [",".join(word) for word in words ]
# print(normal_words)
# upper_words = [word.upper() for word in normal_words]
# print(upper_words)

# print('-' * 20)

# #Convert all the following numbers into positive numbers.

# nums = [44, 64, -12, 0, -5, 34, -55, 67, -88, -99]


# positive_number = [abs (x) for x in nums ]

# print(positive_number)

# print('-' * 20)

# #Flat the following nested list.

# nested_list = [["Hello", "from", "Codezilla"],
# ["Python", "Course", "is", "awesome"],
# ["I", "enjoy", "learning", "Python", "with", "Codezilla"]]

# all_list = [word  for lst in nested_list for word in lst]

# print(all_list)

# print('-' * 20)

# '''Make a list of tuples with the first element as the
# word and the second element as the length of the
# word.'''


# words = ["Hello", "from", "Codezilla", "Python", "Course"]

# element = [(name,len(name)) for index,name in enumerate(words) ]

# print(element)

# print('-' * 20)





# available_fruits = [
#     # Format: [item name, price for kg]
#     ["Apple", 30],
#     ["Banana", 20],
#     ["Orange", 25],
#     ["Mango", 40],
#     ["Strawberry", 35],
#     ["Blueberry", 50],
#     ["Peach", 45],
#     ["Pineapple", 55],
#     ["Watermelon", 30],
#     ["Grapes", 50],
#     ["Cherry", 60],
#     ["Kiwi", 45]
# ]

# basket = []
# price_list  = []
# total = 0
# print('-' * 15)

# while True:
#     welcome = int(input('''Welcome to Diana Fruits Store ! 
#                    1. View Available Fruitd and buy 
#                    2. Total price of basket
#                    3. Quit 
#           Enter the number of your choice :  '''))
#     print(' Available Fruits : ')
#     if welcome == 1:
#         for i , (name,price) in enumerate(available_fruits):
#             print(f'{i + 1}. {name} {price}$ ')
            
#         input_fruits = int(input('Enter The number of the item (0 to retutn to previous menu ) '))
#         if input_fruits == 0:
#             print(welcome)
#         else:
#             print(f'{available_fruits[input_fruits -1][0]} added to basket successfully ')
#             basket.append(available_fruits[input_fruits -1][0])

#     elif welcome == 2:
#         total += available_fruits[input_fruits -1][1]
#         price_list.append(available_fruits[input_fruits -1][1])
        
#         print(f'Total price of basket {total}')
#     elif welcome == 3:
#         if basket:
#             print(f'Total price of basket {total} ')
#             print('Thanks for choosing Diana Fruits Store ')
#             print('See you again soon')
#             item = basket[0],available_fruits[input_fruits -1][1]
            
#             print('Your item is : ')
#             for i in item:
#                 print(f'{i} : {i}',end='\n')
            
#         else:
#             print('Your don\'t have Fruits .... ')
#         break
#     else:
#         print('Error')


    

even_numbers = [ i for i in range(1,11) if i % 2 == 0]
print(even_numbers)