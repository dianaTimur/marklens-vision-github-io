
# drinks = {
#         "Coke": 30,

# "Sprite": 25,
# "Fanta": 25,
# "Pepsi": 30,
# "Tea": 20,
# "Coffee": 25,
# "Orange Juice": 30,
# "Mango Juice": 30
# }

# for drink in drinks:
#     print(drink , drinks[drink])


# menu = {
#  "Cheese pizza": 100,
# "Veggie pizza": 120,
# "Hawaiian pizza": 150,
# "Coke": 30,
# "Sprite": 25,
# "Fanta": 25,
# "Pepsi": 30
# }

# menu['Ice cream'] = 30
# menu['Chocolate cake'] = 60
# menu['Cheese cake'] = 70
# menu['Brownie'] = 40
# menu['Donut'] = 30

# for itemm,price in menu.items():
#     print(itemm, price)



# menu = {
#         "Cheese pizza": 100,

# "Veggie pizza": 120,
# "Hawaiian pizza": 150,
# "Coke": 30,
# "Sprite": 25,
# "Fanta": 25,
# "Pepsi": 30 }
# # for name, price in pizzas.items():
# #     result = (price * 0.20) + price
# #     print(f'{name} : {result:.2f}')

# for item, price in menu.items():
#     print(item)
# # check if the item is a pizza and update the price if "pizza" in item:
#     if 'pizza' in item:
#         menu[item] = price * 1.2
# # print the menu
# for item, price in menu.items():
#         print(f"{item}: {price} EGP")
# pizzas = {"Margherita": 100, "Pepperoni": 120, 
#           "Meat Lovers": 150, "Chicken": 130}

# order = input('What pizza wanted ? ').title()

# if order in pizzas:

#    for name,pirce in pizzas.items():
#       print(f'{order} : {pizzas[order ]+ 20}')
#       break
# else:
#    print('Sorry you Don\'t have thies pizza ')
#    print(f'We have {pizzas.keys()}')


# schools = {
#         "Codezilla School":
# {'1100':"Mohamed Gouda", '1101':"Islam Hesham", 
#  '1102':"Ayman Mohamed", '1103':"Ahmed Khaled"},
# "Al Dorra School":
# {'2100':"Ahmed Hassan", '2101':"Mahmoud Ali",
# '2102':"Adham Wael", '2103':"Khaled Ali"},
# "Mostafa Kamel School":
# {'3105':"Hazem Ahmed", '3106':"Omar Mohamed",
# '3107':"Hussein Kamal", '3109':"Ali Ahmed"}}

# student_name = input('Enter Name : ').title()
# found = True

# for school,names in schools.items():
#     for code , name in names.items():
#         if student_name == name:
#             print(f'The School : {school}')
#             print(f'The Name : {student_name}')
#             print(f'The Code {code}')
#             found = False

# if found:
#     print('The name is don\'t here ...')
       

# employees = {
# "Ahmed Hassan": 12_000,
# "Mohamed Ahmed": 20_000,
# "Ali Ahmed": 15_000,
# "Khaled Ali": 10_000,
# "Omar Mohamed": 13_000,
# "Hazem Ahmed": 24_000,
# 'Diana Omer' : 1_000 }

# for name , price in employees.items():
#     salary = (price * 0.40 ) + price
#     print(f'{name} - {salary}')
