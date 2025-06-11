# students = {
#     'Mohamed' : {
#         'grades' : {
#             'math' : 100,
#             'english' : 90,
#             'science' : 80,
#             'arabic' : 100   
#         }
#     ,'age' : 20}
    
# ,'Ahmed' : {
#     'grades' :{
#         'math' : 80,
#             'english' : 95,
#             'science' : 90,
#             'arabic' : 100
#     },
#     'age' : 21
# }}  

# for name in students:
#     total = 0
#     for grade in students[name]['grades']:
#         total += students[name]['grades'][grade]
#     averge_student = total / len(students[name]['grades'])
#     print(f'The Name is {name} \tAnd The Total is : {total} \tAnd The Averge is : {averge_student}')


# students = {
# "Mohamed": {"grades": [100, 90, 80], "age": 20},
# "Ahmed": {"grades": [100, 95, 93], "age": 21}, 
# "Ali": {"grades": [85, 83, 87], "age": 19}, 
# "Sara": {"grades": [100, 94, 98], "age": 21}
# }

# print(students['Mohamed']['grades'])
# print(students['Ali']['age'])

# for grade in students['Sara']['grades']:
#     print(grade)
#     print(students['Sara']['age'])


# students_school = {
#     'Mohamed':{'grades' : {
#         'math':100,
#         'english' : 90,
#         'science': 80,
#         'arabic' : 100,
#         'history' : 97},
#         'school' : 'Codezilla'

#  }
#     ,'Ahmed' : {
#         'grades':{
#             'math' : 100,
#             'english' : 95,
#             'science' : 93,
#             'arabic' : 100,
#             'history' : 94
#         },
#         'school' : 'Codezilla'
#     }
#     ,'Ali' : {
#         'grades':{
#             'math' : 85,
#             'english' : 83,
#             'science' : 87,
#             'arabic' : 100,
#             'history' : 90
#         }
#     ,'school' : 'Al-Azhar'}

#     ,'Sara' :{
#         'grades' :{
#             'math' : 100,
#             'english' : 94,
#             'science' : 98,
#             'arabic' : 100,
#             'history' : 100
#         }
#     ,'school' : 'Al-Azhar'}
#     }
  
# numbers = []
# total = 0

# for name in students_school['Ali']['grades']:
    
#     total += students_school['Ali']['grades'][name]

# answer = ( total / len(students_school['Ali']['grades'])) * 100


# print(len(students_school['Ali']['grades']))
# print(total)     
# print(f'The percentage of ali is {answer:.2f}%')



# Mohamed grades in math and English
# Mohamed School
# print(f'Name is : Mohamed \t The grades in \nMath {students_school['Mohamed']['grades']['math']}')
# print(f'Name is : Mohamed \t The grades in \nEnglish {students_school['Mohamed']['grades']['english']}' )
# print(f'Mohamed join in school {students_school["Mohamed"]['school']}')

# # Ahmed grades in math, science, and Arabic
# print(f'The name is : Ahmed \tThe grade is math {students_school["Ahmed"]['grades']['math']}')
# print(f'The name is : Ahmed \tThe grade is science {students_school["Ahmed"]['grades']['science']}')
# print(f'The name is : Ahmed \tThe grade is arabic {students_school["Ahmed"]['grades']['arabic']}')

# # Ali school and grades in history, science, and Arabic

# print(f'Name is : Ali , join school is {students_school['Ali']['school']}')
# print(f'The grades is Ali is history {students_school['Ali']['grades']['history']}')
# print(f'The grades is Ali is  science {students_school['Ali']['grades']['science']}')
# print(f'The grades is Ali is  arabic {students_school['Ali']['grades']['arabic']}')

# # Sara grades in math, science, and history


# print(f'Name is Sara \nGrade  is math{students_school['Sara']['grades']['math']}')
# print(f'Name is Sara \nGrade  is science{students_school['Sara']['grades']['science']}')
# print(f'Name is Sara \nGrade  is history{students_school['Sara']['grades']['history']}')


restaurant_menu = {
"Burgers": {"Beef": 100, "Chicken": 80, "Bacon": 120}, "Pizzas": {"Cheese": 100, "Pepperoni": 120, "Veggie": 100}, "Drinks": {"Coke": 20, "Fanta": 20, "Sprite": 20}, "Desserts": {"Ice Cream": 50, "Chocolate Cake": 60,
"Cheese Cake": 70},
"Sides": {"Fries": 30, "Onion Rings": 40, "Potato Wedges": 50
}}

