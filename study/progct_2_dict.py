# students = {
#     "Mohamed Hassan": {"grades": {
#         "math": 100,
#         "english": 90,
#         "science": 80,
#         "arabic": 100,
#         "history": 97},
#         "school": "Codezilla"
#     },
#     "Ahmed Kamal": {"grades": {
# "math": 100,
#     "english": 95,
#     "science": 93,
#     "arabic": 100,
#     "history": 94},
#     "school": "Codezilla"
# },
# "Ali Adel": {"grades": {
#     "math": 98,
#     "english": 100,
#     "science": 100,
#     "arabic": 100,
#     "history": 100},
#     "school": "Al-Azhar"
# },
# "Sare Ahmed": {"grades": {
#     "math": 100,
#     "english": 94,
#     "science": 98,
#     "arabic": 100,
# "history": 100},
#         "school": "Al-Azhar"
#     }
# }


# # highest_name = None
# # highest_number = 0

# # for name in students:
# #     grade = students[name]['grades'].values()
# #     avrage = sum(grade) / len(grade)
# #     if avrage > highest_number:
# #         highest_number = avrage
# #         highest_name = name
        
# # print(highest_name)
# # print(highest_number)
# # if highest_name:
# #     for sub , num in students[highest_name]['grades'].items():
# #         print(f'{sub} : {num}')



# # inventory = {"Paracetamol": {"price":25, "quantity":10}, "Aspirin": {"price":15, "quantity":20},
# # "Ibuprofen": {"price":20, "quantity":15}, "Cough Syrup": {"price":30, "quantity":5}, "Augmentin": {"price":100, "quantity":7}, "Amoxicillin": {"price":80, "quantity":8}, "Panadol": {"price":25, "quantity":10}, "Zinc": {"price":15, "quantity":20}, "Vitamin C": {"price":20, "quantity":15}, "Fucidin": {"price":30, "quantity":5}, "Kolanog": {"price":100, "quantity":2},
# # }
# # choose = ('''Enter your choose 
# #             1. Add new items 
# #             2. Remove items
# #             3. Update itmes
# #             4. Check aveilable quantity 
# #             5. Print treatment information
# #             6. Exit \t''')
# # while True:
# #     number = input(choose)
# #     if number == '1':
# #         item_name = input('Enter item name (press Enter to Exit) : ').title()
# #         if item_name:
# #             item_price = float(input('Enter item price : '))
# #             item_quantity = int(input('Enter item quantity : '))
# #             inventory.update({item_name:{'price' : item_price , 'quantity' : item_quantity}})
# #             print(f'It has been added {item_name}')
# #         else:
# #             input(choose)
# #     elif number == '2':
# #         item_name = input('Enter item to be deleted ').title()
# #         if item_name in inventory.keys():
# #             sure = input(f'Are you sure you wan\'t delete {item_name} (Y/N)')
# #             match sure.lower():
# #                 case 'y' | 'yes':
# #                     del inventory[item_name]
# #                     print(f'{item_name} has been deleted ')
# #                 case _:
# #                     input(choose)
# #     elif number == '3':
# #         item_name = input('Enter item name to be updated ...(press Enter to Exit)').title()
# #         if item_name:
# #             item_price = float(input('Enter the new price : '))
# #             item_quantity = int(input('Enter the new quantity : '))
# #             inventory[item_name] ={ 'price' : item_price , 'quantity': item_quantity }
# #             print(f' {item_name} has been updated ')
# #         else:
# #             input(choose)
# #     elif number == '4':
# #         item_name = input('Enter item to be cecked quantity : ').title()
# #         if item_name in inventory :
# #             print(f'We have {inventory[item_name]['quantity']} {item_name} units ')
# #     elif number == '5':
# #         item_name  = input('Enter item name : ').title()
# #         if item_name in inventory:
# #             print(f'Item : {item_name}')
# #             print(f'Price : {inventory[item_name]['price']}')
# #             print(f'Quantity : {inventory[item_name]['quantity']}')
# #         else:
# #             print(f'{item_name} is not found')
# #     elif number == '6':
# #         print('Have a nice day ! ')
# #         break
# #     else:
# #         input(choose)



# # schools = {
# #     "Codezilla":
# #         {"Mohamed Hassan":
# #             {"math": 100,
# #         "english": 90,
# #         "science": 85,
# #         "arabic": 100,
# #         "history": 97},
# #     "Ahmed Kamal":
# #         {"math": 100,
# #         "english": 95,
# #         "science": 93,
# #         "arabic": 100,
# #         "history": 94}
# # },    
# # "Al-Azhar":{
# #     "Ali Adel": {
# #         "math": 85,
# #         "english": 83,
# #         "science": 87,
# #         "arabic": 100,
# #         "history": 90},
# #     'Mariam Ali':{
# #     "math": 100,
# # "english": 94,
# # "science": 98,
# # "arabic": 100,
# # "history": 100}},
# # }


# # for school_name , studnets in schools.items():
# #     total_school = 0
# #     student_count = 0
# #     for studnet , grade in studnets.items():
# #         averge_student = sum(grade.values()) / len(grade)
# #         total_school += averge_student
# #         student_count += 1
# #     if student_count > 0:
# #         averge_school = total_school / student_count
# #         print(f'The Average Total Percentage for {school_name} school is {averge_school:.2f} ')
# #     else:
# #         continue



# # students = {
# #     "Mohamed Hassan": {"grades": {
# #         "math": 100,
# #         "english": 90,
# #         "science": 80,
# #         "arabic": 100,
# #         "history": 97},
# #         "school": "Codezilla"
# # },
# # "Ahmed Kamal": {"grades": {
# #     "math": 100,
# #     "english": 95,
# #     "science": 93,
# #     "arabic": 100,
# #     "history": 94},
# #     "school": "Codezilla"
# # },
# # "Ali Adel": {"grades": {
# #     "math": 85,
# #     "english": 83,
# #     "science": 87,
# #     "arabic": 100,
# #     "history": 90},
# #     "school": "Al-Azhar"
# # },
# # "Hossam Yehia": {"grades": {
# #     "math": 100,
# #     "english": 94,
# #     "science": 98,
# # "arabic": 100,
# # "history": 100},
# # "school": "Al-Azhar"},
# # 'diana' : {'grades' : {
# #     "math": 99,
# #     "english": 99,
# #     "science": 97,
# #     "arabic": 100,
# #     "history": 80}
    
# # }}



# # total = 0
# # name_hig = ''

# # for name in students:
# #     grades_list = list(students[name]['grades'].values())
# #     higst_number = sum(grades_list) / len(grades_list)
# #     if higst_number > total:
# #         total = higst_number
# #         name_hig = name
# # print(f'{name_hig} is have {total} % ')
# # for subject , grade in students[name_hig]['grades'].items():
# #     print(f'{subject} : {grade}')




# hot_drinks = {"Coffee": 20, "Tea": 15, "Hot Chocolate": 25} 
# cold_drinks = {"Soda": 10, "Iced Tea": 15, "Smoothie": 30} 
# desserts = {"Ice Cream": 50, "Chocolate Cake": 60 ,"Cheesecake": 70}


# menu = {'Hot Drinks' : hot_drinks ,'Cold Drinks' : cold_drinks,'Desserts' : desserts}
# order = {}


# print('Welcome The Diana Coffee ! ')

# while True:
#     print('-' * 20)
#     for i , name_menu in enumerate(menu):
#         print(f'{i + 1}. {name_menu} ')
    
#     user_choice = input('Please, Enter the number of the item Type \
#                     (Enter to Exit) : ')
#     if user_choice == '':
#         break
#     index_user_choice = list(menu)[int(user_choice) - 1]
#     name_index_user_choice = (menu[index_user_choice])
#     for x , name_item in enumerate(name_index_user_choice):
#         item_price = name_index_user_choice[name_item]
#         print(f'{x + 1}. {name_item} : {item_price}$ ')
#     user_choice_item = input('Enter Item Number : ')
#     index_user_choice_item = list(name_index_user_choice)[int(user_choice_item) - 1]
#     price_item = name_index_user_choice[index_user_choice_item]

#     quantity = int(input('Please Enter Quantity : '))
#     result =   price_item * quantity

#     order[index_user_choice_item] = {'price':price_item, 'quantity': quantity, 'total' : result}

# all_total = [order[name]['total'] for name in order]
# sum_total = sum(all_total)
# for NAME in order:
#     print(f"""
#           Item : {NAME}
#           Price : {order[NAME]['price']}
#           Quantity : {order[NAME]['quantity']}
#           Total : {order[NAME]['total']}         
#           Total Order is : {sum_total} """)


